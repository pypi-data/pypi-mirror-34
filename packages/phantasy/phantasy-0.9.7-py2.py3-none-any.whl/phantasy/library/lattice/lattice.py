#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Create high-level lattice object from machine configuration files.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import logging
import os
import shelve
import sys
import tempfile
import time
from collections import OrderedDict
from datetime import datetime
from fnmatch import fnmatch
from math import log10

import numpy as np
from flame import Machine

from phantasy.library.layout import Layout
from phantasy.library.layout import build_layout
from phantasy.library.misc import bisect_index
from phantasy.library.misc import flatten
from phantasy.library.misc import get_intersection
from phantasy.library.misc import parse_dt
from phantasy.library.misc import pattern_filter
from phantasy.library.model import BeamState
from phantasy.library.model import ModelFlame
from phantasy.library.parser import Configuration
from phantasy.library.settings import Settings
from phantasy.library.settings import build_flame_settings
from phantasy.library.physics import get_orbit
from phantasy.library.physics import inverse_matrix
from .element import AbstractElement
from .element import CaElement
from .flame import FlameLatticeFactory
from .impact import LatticeFactory as ImpactLatticeFactory
from .impact import run_lattice as run_impact_lattice

_LOGGER = logging.getLogger(__name__)

try:
    basestring
except NameError:
    basestring = str

try:
    r_input = raw_input
except NameError:
    r_input = input


class Lattice(object):
    """Machine high-level lattice object, all elements inside this lattice
    has an unique name.

    Parameters
    ----------
    name : str
        Lattice name.

    Keyword Arguments
    -----------------
    s_begin : float
        Start position along beam trajectory, [m].
    s_end : float
        End position along beam trajectory, [m].
    mname : str
        Name of loaded machine, from which lattice itself is loaded.
    mpath : str
        Path name of machine configurations.
    mconf : obj
        Machine configuration object.
    mtype : int
        Machine type, 0 for linear (default), 1 for a ring.
    source : str
        Source of PV data, URL of channel finder service, file name of SQLite
        database or csv spreadsheet.
    length : float
        Total length of lattice, if 'mtype' is 1, refers to circumference.
    model : str
        Model type (case insensitive), or code name for simulation, 'FLAME'
        or 'IMPACT', the former is the default one.
    data_dir: str
        Path of directory to host data generated from model, including input
        lattice files, output files and other related files, if not defined,
        random folder will be created in system temporary directory,
        e.g.'/tmp/model_hGe1sq'.
    config :
        Lattice configuration object.
    layout :
        Lattice layout object.
    settings :
        Lattice settings object.
    model_factory :
        Lattice factory object for online model.
    trace : str
        If 'on', history of PV set actions could be traced back, or ('off')
        set action cannot be reverted, by default, trace feature is on.
    group : dict
        Initial group configuration.

    Note
    ----
    :class:`~phantasy.library.operation.create_lattice` could be used to
    set up lattice created by this class by provided information like: PV data,
    lattice layout, configuration and settings, etc.

    See Also
    --------
    :func:`~phantasy.library.operation.lattice.create_lattice`
        Create high-level lattice object.
    """

    def __init__(self, name, **kws):
        self.name = name
        self.source = kws.get('source', None)
        self.s_begin = kws.get('s_begin', None)
        self.s_end = kws.get('s_end', None)
        self.mname = kws.get('mname', None)
        self.mpath = kws.get('mpath', None)
        self.mconf = kws.get('mconf', None)
        self.mtype = kws.get('mtype', None)
        self.length = kws.get('length', None)
        self.model = kws.get('model', None)
        self.data_dir = kws.get('data_dir', None)
        self.layout = kws.get('layout', None)
        self.config = kws.get('config', None)
        self.settings = kws.get('settings', None)
        self.model_factory = kws.get('model_factory', None)
        self.group = kws.get('group', None)

        self._viewer_settings = OrderedDict()
        self._trace_history = None
        self.trace = kws.get('trace', None)
        self._elements = []
        self._orm = None

        # clean up the following parameters
        self.isring = bool(self.mtype)
        self.latticemodelmap = None

    @property
    def group(self):
        """dict: Group configuration."""
        return self._group

    @group.setter
    def group(self, g):
        if g is None:
            self._group = dict()
        elif isinstance(g, dict):
            self._group = g
        else:
            _LOGGER.warning("'group' attribute is always initialized with {}.")

    @property
    def trace(self):
        """str: Keep/revert history feature flag for PV set actions."""
        return self._trace

    @trace.setter
    def trace(self, trace):
        if trace is None or trace == 'on':
            self._trace = 'on'
            if self._trace_history is None:
                self._trace_history = []
        else:
            self._trace = 'off'
            if self._trace_history is not None:
                self._trace_history = None

    @property
    def config(self):
        """Obj: Lattice configuration object."""
        return self._config

    @config.setter
    def config(self, config):
        if config is not None and isinstance(config, Configuration):
            self._config = config
        else:
            self._config = self._get_default_config()

    @property
    def layout(self):
        """Obj: Accelerator layout object."""
        return self._layout

    @layout.setter
    def layout(self, layout):
        if layout is not None and isinstance(layout, Layout):
            self._layout = layout
        else:
            self._layout = self._get_default_layout()

    @property
    def settings(self):
        """Obj: Lattice settings object."""
        return self._settings

    @settings.setter
    def settings(self, settings):
        if settings is not None and isinstance(settings, Settings):
            self._settings = settings
        else:
            self._settings = self._get_default_settings()
        # update model factory
        self.model_factory = None

    @property
    def model_factory(self):
        """Obj: Lattice factory of defined model type."""
        return self._model_factory

    @model_factory.setter
    def model_factory(self, mf):
        if mf is None:
            self._model_factory = self._set_model_factory()
        elif self.model == "FLAME" and isinstance(mf, FlameLatticeFactory):
            self._model_factory = mf
        elif self.model == "IMPACT" and isinstance(mf, ImpactLatticeFactory):
            self._model_factory = mf
        else:
            raise TypeError("Wrong input model factory.")

    @property
    def s_begin(self):
        """float: Start position along beam trajectory, [m]."""
        return self._s_begin

    @s_begin.setter
    def s_begin(self, s):
        if s is None:
            self._s_begin = 0.0
        else:
            self._s_begin = s

    @property
    def s_end(self):
        """float: End position along beam trajectory, [m]."""
        return self._s_end

    @s_end.setter
    def s_end(self, s):
        if s is None:
            self._s_end = sys.float_info.max
        else:
            self._s_end = s

    @property
    def mname(self):
        """str: Name of loaded machine, from which lattice itself is loaded."""
        return self._mname

    @mname.setter
    def mname(self, name):
        if name is None:
            from phantasy.library.dconf import _DEMO_MNAME
            self._mname = _DEMO_MNAME
        else:
            self._mname = name

    @property
    def mpath(self):
        """str: Path name of machine configurations."""
        return self._mpath

    @mpath.setter
    def mpath(self, path):
        if path is None:
            from phantasy.library.dconf import _DEMO_MPATH
            self._mpath = _DEMO_MPATH
        else:
            self._mpath = path

    @property
    def mconf(self):
        """Obj: Machine configuration object."""
        return self._mconf

    @mconf.setter
    def mconf(self, config):
        if isinstance(config, Configuration):
            self._mconf = config
        else:
            from phantasy.library.dconf import _DEMO_MCONF
            self._mconf = _DEMO_MCONF

    @property
    def mtype(self):
        """int: Machine type, linear (0) or circular (1)."""
        return self._mtype

    @mtype.setter
    def mtype(self, i):
        if i is None:
            self._mtype = 0
        else:
            self._mtype = i

    @property
    def source(self):
        """str: Source of PV data."""
        return self._source

    @source.setter
    def source(self, src):
        if src is None:
            self._source = None
        else:
            self._source = src

    @property
    def length(self):
        """Total length of lattice, if 'mtype' is 1, refers to circumference."""
        return self._length

    @length.setter
    def length(self, s):
        if s is None:
            self._length = 0.0
        else:
            self._length = s

    @property
    def model(self):
        """str: Code name to simulate online model type, *FLAME* by default."""
        return self._model

    @model.setter
    def model(self, code):
        if code is None:
            self._model = "FLAME"
        else:
            self._model = code.upper()

    @property
    def data_dir(self):
        """str: Path of directory to host data generated from model."""
        return self._data_dir

    @data_dir.setter
    def data_dir(self, path):
        if path is None:
            systmp = '/tmp'
            self._data_dir = tempfile.mkdtemp(prefix='model_', dir=systmp)
        else:
            self._data_dir = path

    def _get_default_config(self):
        if self.mconf.has_option(self.name, "config_file"):
            configfile = self.mconf.getabspath(self.name, "config_file")
            config = Configuration(configfile)
        else:
            from phantasy.library.dconf import _DEMO_MCONFIG
            config = _DEMO_MCONFIG
        return config

    def _get_default_settings(self):
        if self.mconf.has_option(self.name, "settings_file"):
            settingfile = self.mconf.getabspath(self.name, "settings_file")
            settings = Settings(settingfile)
            _LOGGER.debug("Apply settings file from machine configs.")
        else:
            settings = None
        return settings

    def _get_default_layout(self):
        if self.mconf.has_option(self.name, "layout_file"):
            layoutfile = self.mconf.getabspath(self.name, "layout_file")
            layout = build_layout(layoutfile)
        else:
            layout = None
        return layout

    def _set_model_factory(self):
        if self.model == "IMPACT":
            mf = ImpactLatticeFactory(self.layout, config=self.config,
                                      settings=self.settings)
        elif self.model == "FLAME":
            mf = FlameLatticeFactory(self.layout, config=self.config,
                                     settings=self.settings)
        else:
            raise RuntimeError(
                "Lattice: Model '{}' not supported".format(self.model))
        return mf

    def get_model_settings(self, only_physics=False):
        """Get settings from 'model' environment, if *only_physics* is `True`,
        only return physics field settings, otherwise return both engineering
        and physics settings.

        Parameters
        ----------
        only_physics : bool
            If `True`, only return physics settings, the same as `settings`
            attribute, the default value is `False`.

        Returns
        -------
        r :
            Settings object.

        See Also
        --------
        :func:`~phantasy.library.settings.common.generate_settings`
        """
        if only_physics:
            return self.settings
        else:
            all_settings = Settings()
            for e_name, e_phyconf in self.settings.items():
                elem = self._find_exact_element(e_name)
                all_settings.update(OrderedDict({e_name: e_phyconf}))
                for phy_fld_name in set(e_phyconf).intersection(
                        elem.get_phy_fields()):
                    eng_fields = elem.get_eng_fields()
                    if len(eng_fields) == 1:
                        all_settings[e_name].update(
                            {eng_fields[0]:
                                 elem._unicorn_p2e(e_phyconf[phy_fld_name])})
            return all_settings

    def set(self, elem, value, field=None, **kws):
        """Set the value of a lattice element field, if element only has one
        field, parameter *field* is optional, or *field* must be specified.

        Parameters
        ----------
        elem : str or CaElement object
            Element name string or CaElement object.
        value :
            Value of the field, type should be valid w.r.t *field*.
        field : str
            Field name (case insensitive) of element to be assigned, optional
            if element has only one field, *value* will be assigned to.

        Keyword Arguments
        -----------------
        source : str
            Three options available: 'all', 'control' and 'model', by default
            'all', i.e. update both 'control' and 'model' environment.

        Returns
        -------
        ret :
            None if failed, or 0.
        """
        elems = self._get_element_list(elem)
        if len(elems) != 1:
            raise RuntimeError(
                "Lattice: Multiple elements found with the specified name.")
        _elem = elems[0]

        all_fields = _elem.fields

        if len(all_fields) > 1:
            if field is None:
                print("Please specify field from [{}]".format(
                    ','.join(all_fields)))
                return None
            elif field not in all_fields:
                print("Wrong field.")
                return None
        elif len(all_fields) == 1:
            field = all_fields[0]
        else:
            print("Element does not have the defined field.")
            return None

        source = kws.get('source', 'all')
        if source == 'all':
            self._set_control_field(_elem, field, value)
            self._set_model_field(_elem, field, value)
        elif source == 'control':
            self._set_control_field(_elem, field, value)
        elif source == 'model':
            self._set_model_field(_elem, field, value)
        else:
            raise RuntimeError("Invalid source.")

        return 0

    def _set_control_field(self, elem, field, value):
        """Set value to element field onto control environment.
        """
        value0 = elem.last_settings.get('field')
        if value0 is None:
            value0 = getattr(elem, field)
        if elem.family == "CAV" and field == 'PHA':
            value = _normalize_phase(value)
        setattr(elem, field, value)
        self._log_trace('control', element=elem.name,
                        field=field, value0=value0, value=value)

    def _set_model_field(self, elem, field, value):
        """Set value to element field.
        """
        if isinstance(elem, CaElement):
            elem_name = elem.name
        else:
            elem_name = elem
        if elem_name not in self.settings:
            _LOGGER.warning(
                "Element:{} to set not found in lattice model.".format(
                    elem_name))
        elif field not in self.settings[elem_name]:
            _LOGGER.warning(
                "Field: {} to set not found in element: {}.".format(
                    field, elem_name))
        else:
            value0 = self.settings[elem_name][field]
            self.settings[elem_name][field] = value
            self.model_factory.settings[elem_name][field] = value
            _LOGGER.debug(
                "Updated field: {0:s} of element: {1:s} with value: {2:f}.".format(
                    field, elem_name, value))
        self._log_trace('model', element=elem_name, field=field,
                        value=value, value0=value0)

    def _log_trace(self, type, **kws):
        """Add set log entry into trace history.

        Parameters
        ----------
        type : str
            Set type according to environment source, 'control' or 'model'.
        timestamp
        element
        field
        value
        value0
        """
        if self._trace == 'on':
            name = kws.get('element')
            field = kws.get('field')
            value = kws.get('value')
            value0 = kws.get('value0')
            log_entry = OrderedDict((
                ('timestamp', time.time()),
                ('type', type),
                ('element', name),
                ('field', field),
                ('value0', value0),
                ('value', value),
            ))
            self._trace_history.append(log_entry)
        else:
            pass

    def get(self, elem, field=None, **kws):
        """Get the value of a lattice element field.

        Parameters
        ----------
        elem : str or CaElement object
            Element name string or CaElement object.
        field : str
            Field name (case insensitive) of element, if not defined, all
            field names will be selected.

        Keyword Arguments
        -----------------
        source : str
            Two options available: 'control' and 'model', by default 'control'
            i.e. only get from 'control' environment.
        mstate : bool
            If True, return BeamState instance, False by default, only
            valid for viewer elements and ``source='model'``.

        Note
        ----
        If ``source`` is defined as ``'model'``, settings will be retrieved
        from model environment, there are two categories: one is devices that
        accept new values settings, e.g. corrector, cavity, etc., the other is
        devices that only can show readings, e.g. BPM, PM, etc. (so-called
        *viewer elements*). For *viewer elements*, ``BeamState`` could be
        got after ``run()``, for flame model.

        Returns
        -------
        ret : dict
            Field value, {field: value}.
        """
        elems = self._get_element_list(elem)
        if len(elems) != 1:
            raise RuntimeError(
                "Lattice: Multiple elements found with the specified name.")
        _elem = elems[0]
        all_fields = _elem.fields
        if field is None:
            field = all_fields
        elif field not in all_fields:
            print("Wrong field.")
            return None

        source = kws.get('source', 'control')

        if source == 'control':
            retval = _get_control_field(_elem, field)
        elif source == 'model':
            mstate_flag = kws.get('mstate', False)
            retval = self._get_model_field(_elem, field, mstate=mstate_flag)
        else:
            raise RuntimeError("Invalid source.")

        return retval

    def _get_model_field(self, elem, field, **kws):
        """Get field value(s) from elment.

        Keyword Arguments
        -----------------
        mstate : bool
            If True, return BeamState instance, False by default.
        """
        if not isinstance(field, (list, tuple)):
            field = field,
        elem_name = elem.name
        if _is_viewer(elem):
            _settings = self._viewer_settings
        else:
            _settings = self.settings
        retval = {k: v for k, v in _settings[elem_name].items() if k in field}
        if kws.get('mstate', False) and _is_viewer(elem):
            retval['mstate'] = self._viewer_settings[elem_name]['mstate']
        return retval

    def trace_history(self, rtype='human', **kws):
        """Inspect trace history of Lattice set actions, return data type with
        human friendly or raw format.

        Parameters
        ----------
        rtype : str
            'human' or 'raw', default option 'human' will return formated
            human readable strings, could be printed out to streams;
            'raw' will return history entries meeting filters defined by
            keyword arguments.

        Note
        ----
        Data structure of every traced log entry:

        +---------------+--------------------------------------+
        |  key name     |   value example                      |
        +---------------+--------------------------------------+
        | *timestamp*   | ``1485275869``                       |
        +---------------+--------------------------------------+
        | *type*        | ``control``                          |
        +---------------+--------------------------------------+
        | *element*     | ``LS1_CA01:CAV1_D1127``              |
        +---------------+--------------------------------------+
        | *field*       | ``PHA``                              |
        +---------------+--------------------------------------+
        | *value*       | ``30``                               |
        +---------------+--------------------------------------+
        | *value0*      | ``325``                              |
        +---------------+--------------------------------------+

        Keyword Arguments
        -----------------
        element : str
            Unix shell pattern of element name.
        field : str
            Unix shell pattern of element field name.
        type : str
            Log entry type: 'control' or 'model', could be Unix shell pattern.
        value : number or list of numbers
            From which, lower and upper limit values will be extracted.
        """
        if self._trace_history is None:
            return None

        _history = self._filter_trace(self._trace_history, **kws)

        if rtype == 'human':
            retval = []
            for log_entry in _history:
                type = log_entry['type']
                ts = log_entry['timestamp']
                value = log_entry['value']
                value0 = log_entry['value0']
                name = log_entry['element']
                field = log_entry['field']
                log_str = "{ts} [{type:^7s}] Set {name:<22s} TO {value:<10.3f} [{value0:^10.3f}]".format(
                    ts=datetime.fromtimestamp(ts).strftime(
                        '%Y-%m-%d %H:%M:%S'),
                    type=type, name="{0} [{1}]".format(name, field),
                    value=value, value0=value0)
                retval.append(log_str)
                print(log_str)
            return "\n".join(retval)
        else:
            return _history

    @staticmethod
    def _filter_trace(data, **kws):
        """Apply filters on trace history data, return list of valid entries.
        """
        # filters
        elem_name = kws.get('element', '*')
        pv_name = kws.get('pv', None)
        entry_type = kws.get('type', '*')
        field_name = kws.get('field', '*')
        value = kws.get('value', None)
        if value is not None:
            if isinstance(value, (int, float, long)):
                value = [value]
            elif not isinstance(value, (list, tuple)):
                raise RuntimeError("Invalid value argument.")
            val_min, val_max = min(value), max(value)
        else:
            val_min, val_max = -1e10, 1e10

        retval = []
        for d in data:
            _elem_name = d.get('element')
            _pv_name = d.get('pv', None)
            _entry_type = d.get('type')
            _field_name = d.get('field')
            _value = d.get('value')
            if Lattice._fnmatch(_pv_name, pv_name) \
                    and fnmatch(_elem_name, elem_name) \
                    and fnmatch(_entry_type, entry_type) \
                    and fnmatch(_field_name, field_name) \
                    and val_min <= _value <= val_max:
                retval.append(d)

        return retval

    @staticmethod
    def _fnmatch(name, pattern):
        if pattern is None:  # pv pattern is not defined
            return True
        else:  # pv pattern is defined
            if name is None:
                return False
            else:
                return fnmatch(name, pattern)

    def roll_back(self, setting=None, type=None, retroaction=None):
        """Roll back PV setpoint by providing *setting* or log entries from
        trace history, which indicating high-level lattice object to proceed
        some set action to roll it back into previous states.

        Parameters
        ----------
        setting : dict of list of dict
            Element setting, could be trace_history entry, if not defined,
            use the last entry with the type of 'control'
        type : str
            Type of environment to roll back, 'control' or 'model', 'control'
            by default.
        retroaction : time
            Timestamp of the trace history, dating back to *retroaction*,
            machine state should roll back to be.

        Note
        ----
        Possible input of *setting* parameter:
        - (Default) Last trace history entry.
        - Trace history entry or list of entries;

        Note
        ----
        About *retroaction* parameter, following input types will be supported:

        - Absolute timestamp indicated by a float number, i.e. time in seconds
          since Epoch: entries with logging timestamp newer (bigger) than
          *retroaction* will be rolled back;
        - Relative timestamp w.r.t. current time available units: *years*,
          *months*, *weeks*, *days*, *hours*, *minutes*, *seconds*,
          *microseconds*, and some unit alias: *year*, *month*, *week*, *day*,
          *hour*, *minute*, *second*, *microsecond*, *mins*, *secs*, *msecs*,
          *min*, *sec*, *msec*, could be linked by string 'and' or ',',
          ended with 'ago', e.g. '5 mins ago', '1 hour and 30 mins ago'.

        Warning
        -------
        If valid *retroaction* parameter is defined, *setting* will be
        disregarded.

        See Also
        --------
        trace_history : Log history of set actions.
        """
        stype = 'control' if type is None else type
        _history = self.trace_history(rtype='raw', type=stype)
        if setting is None:
            if _history != []:
                setting = _history[-1]

        if retroaction is not None:
            setting = _get_retroactive_trace_history(_history, retroaction)

        if not isinstance(setting, (list, tuple)):
            setting = setting,

        for entry in setting:
            _elem_name = entry.get('element')
            _entry_type = entry.get('type')
            _field_name = entry.get('field')
            _value = entry.get('value0')
            self.set(_elem_name, _value, _field_name, source=_entry_type)

    def update_model_settings(self, model_lattice, **kws):
        """Update model lattice settings with external lattice file, prefer
        keyword argument *sdict* or *sjson* if any one is defined.

        Parameters
        ----------
        model_lattice : path
            External model lattice file.

        Keyword Arguments
        -----------------
        sdict : dict
            Dict of model lattice settings.
        sjson : path
            JSON file of model lattice settings.
        """
        sdict = kws.get('sdict', None)
        sjson = kws.get('sjson', None)
        if isinstance(sdict, dict):
            settings = sdict
        elif sjson is not None:
            with open(sjson, 'r') as fp:
                settings = json.load(fp)
        else:
            # read settings from lattice file
            if self.model == 'FLAME':
                settings = build_flame_settings(model_lattice)
            elif self.model == 'IMPACT':
                raise NotImplementedError

        # apply settings
        for e_name, e_setting in settings.items():
            if e_name in self.settings:
                for field, value in e_setting.items():
                    self._set_model_field(e_name, field, value)
                    _LOGGER.debug("Update model: {e}:{f} to be {v}.".format(
                        e=e_name, f=field, v=value))
            else:
                _LOGGER.debug(
                    'Model settings does not have field: {e}:{f}.'.format(
                        e=e_name, f=field))

    def sync_settings(self, data_source=None):
        """Synchronize lattice settings between model and control environment.

        Parameters
        ----------
        data_source : str
            Data source of synchronization, if 'model' is defined, will update
            data of control environment with data from 'model'; if 'control'
            is defined, model data will be synchronized; *data_source* is
            'control' by default.
        """
        data_source = 'control' if data_source is None else data_source

        if data_source == 'control':
            _LOGGER.info("Sync settings from 'control' to 'model'.")
            model_settings = self.settings
            for elem in self._get_element_list('*'):
                if elem.name in model_settings:
                    if not self._skip_elements(elem.name):
                        for field, value in self.get(elem=elem,
                                                     source='control').items():
                            if field in model_settings[elem.name]:
                                self._set_model_field(elem, field, value)
                            else:
                                _LOGGER.debug(
                                    'Model settings does not have field: {e}:{f}.'.format(
                                        e=elem.name, f=field))
                else:
                    _LOGGER.debug(
                        'Model settings does not have element: {e}.'.format(
                            e=elem.name))
        elif data_source == 'model':
            _LOGGER.info("Sync settings from 'model' to 'control'.")
            for e_name, e_setting in self.settings.items():
                elem = self._get_element_list(e_name)
                if elem == []:
                    _LOGGER.debug(
                        'Control settings does not have element {0}.'.format(
                            e_name))
                    continue
                for field, value in e_setting.items():
                    if not self._skip_elements(elem[0].name):
                        if field in elem[0].fields:
                            self._set_control_field(elem[0], field, value)

    def load_settings(self, settings=None, stype='design'):
        """Initializing design settings of elements from *settings*.

        Parameters
        ----------
        settings :
            Settings object.
        stype : str
            Setting type, 'design' or 'last', to set `design_settings` or
            `last_settings`, respectively.
        """
        settings = self.settings if settings is None and \
                                    self.settings is not None else settings
        if settings is None:
            _LOGGER.warning("Cannot load settings from None.")
            return 0
        for k, v in settings.items():
            el = self._find_exact_element(k)
            if el is not None:
                if stype == 'design':
                    el.design_settings.update(dict(v))
                elif stype == 'last':
                    el.last_settings.update(dict(v))
                _LOGGER.debug(
                    "Updated {0:<20}: {1}_settings.".format(el.name, stype))

    def _skip_elements(self, name):
        """Presently, element should skip: SEXT
        """
        SKIP_TYPES = ['SEXT']
        elements = self.model_factory._accel.elements
        for e in elements:
            if e.name == name:
                return e.ETYPE in SKIP_TYPES

    def run(self):
        """Run machine with defined model, e.g. 'FLAME' or 'IMPACT',
        update model settings, but not control settings.

        Returns
        -------
        ret : tuple
            tuple of (path, model), path of the model data directory and model
            object.
        """
        if self.model == "IMPACT":
            lat = self._latticeFactory.build()
            config = self._latticeFactory.config
            work_dir = run_impact_lattice(lat, config=config,
                                          work_dir=self.data_dir)
            if self.latticemodelmap is None:
                self.createLatticeModelMap(os.path.join(work_dir, "model.map"))
            return work_dir, None
        elif self.model == "FLAME":
            lat = self.model_factory.build()
            _, latpath = tempfile.mkstemp(prefix='model_', suffix='.lat',
                                          dir=self.data_dir)
            with open(latpath, 'w') as f:
                lat.write(f)
            fm = self._flame_model(latconf=lat.conf())
            return latpath, fm
        else:
            raise RuntimeError(
                "Lattice: Simulation code '{}' not supported".format(
                    self.model))

    def _flame_model(self, **kws):
        """Create a new flame model
        """
        latconf = kws.get('latconf', None)
        latfile = kws.get('latfile', None)

        if latconf is not None:
            m = Machine(latconf)
        elif latfile is not None:
            m = Machine(open(latfile, 'r'))
        ms = BeamState(machine=m)
        fm = ModelFlame()
        fm.mstates, fm.machine = ms, m
        obs = fm.get_index_by_type(type='bpm')['bpm']
        r, s = fm.run(monitor=obs)
        self._update_viewer_settings(fm, r)
        return fm

    def _update_viewer_settings(self, fm, r):
        """Initially, all viewer settings are {}, after ``run()``,
        new key-values will be added into.

        field : model environment
        key   : flame model
        +---------+----------+-----------+
        |  Family | field    |  key      |
        +---------+----------+-----------+
        |  BPM    |   X [m]  |  x0 [mm]  |
        |  BPM    |   Y [m]  |  y0 [mm]  |
        +---------+----------+-----------+
        """
        for i, res in r:
            elem_name = fm.get_element(index=i)[0]['properties']['name']
            readings = {field: getattr(res, k)[0] * 1e-3 for field, k in
                        zip(['X', 'Y'], ['x0', 'y0'])}
            readings['mstate'] = res
            self._viewer_settings[elem_name] = readings

    def __getitem__(self, i):
        if isinstance(i, basestring):
            return self._find_exact_element(i)
        else:
            return self._elements[i]

    def __len__(self):
        return len(self._elements)

    def _find_exact_element(self, name):
        """Return element object if *name* is fully matched, or return None.
        """
        if isinstance(name, AbstractElement):
            name = name.name
        for e in self._elements:
            if str(e.name) == str(name):
                return e
        return None

    def get_elements(self, name=None, type=None, srange=None, **kws):
        """Get element(s) with defined filter rules.

        Parameters
        ----------
        name : str or list[str]
            (List of) Element names or Unix shell style patterns.
        type : str or list[str]
            (List of) Element type/group/family, or Unix shell style patterns.
        srange : tuple
            Start and end points (tuple of float) of elements' longitudinal
            position.

        Keyword Arguments
        -----------------
        sort_key : str
            Ascendingly sort key of the returned list, ``name`` or ``pos``,
            ``pos`` by default, or other attributes valid for ``CaElement``.

        Returns
        -------
        ret : List
            List of elements (``CaElement``), excluding virtual elements.

        Note
        ----
        1. The pattern here used is Unix shell style, slightly different
           from regex, e.g. pattern 'BP' matches 'BPM' in regex, but matches
           nothing in Unix shell style, 'BP*' works;
        2. If more than one positional parameters (*name*, *type*, *srange*)
           are defined, return elements that meet all definitions;
        3. By default, the returned elements are ascendingly sorted according
           to element position values.

        Examples
        --------
        1. Define *name* with an invalid name:

        >>> get_elements(name='NOEXISTS')
        []

        2. Define *name* with name or name patterns:

        >>> get_elements(name='FS1_BMS:DCV_D2662')
        [FS1_BMS:DCV_D2662 [VCOR] @ sb=153.794690]
        >>> get_elements(name=['FS1_B?*D266?', 'LS1_B*DCV*'])
        [LS1_BTS:DCV_D1937 [VCOR] @ sb=81.365954,
         LS1_BTS:DCV_D1964 [VCOR] @ sb=84.013954,
         LS1_BTS:DCV_D1997 [VCOR] @ sb=87.348954,
         LS1_BTS:DCV_D2024 [VCOR] @ sb=90.055166,
         LS1_BTS:DCV_D2061 [VCOR] @ sb=93.710487,
         LS1_BTS:DCV_D2114 [VCOR] @ sb=98.985556,
         FS1_BMS:DCV_D2662 [VCOR] @ sb=153.794690,
         FS1_BMS:DCH_D2662 [HCOR] @ sb=153.794690,
         FS1_BMS:BPM_D2664 [BPM] @ sb=153.963690,
         FS1_BMS:QH_D2666 [QUAD] @ sb=154.144690]

        3. Filter BPMs from the above result:

        >>> get_elements(name=['FS1_B?*D266?', 'LS1_B*DCV*'], type='BPM')
        [FS1_BMS:BPM_D2664 [BPM] @ sb=153.963690]
        >>> # type='BPM' also could be pattern

        4. Filter hybrid types:

        >>> get_elements(name=['FS1_B?*D266?', 'LS1_B*DCV*'],
        >>>              type=['BPM', 'QUAD'])
        [FS1_BMS:BPM_D2664 [BPM] @ sb=153.963690,
         FS1_BMS:QH_D2666 [QUAD] @ sb=154.144690]

        5. Get subsection from lattice according to s-position range:

        >>> get_elements(srange=(10, 11))
        [LS1_CB01:CAV1_D1229 [CAV] @ sb=10.366596,
         LS1_CB01:BPM_D1231 [BPM] @ sb=10.762191,
         LS1_CB01:SOL1_D1235 [SOL] @ sb=10.894207]

        6. Continue filter with *srange* parameter

        >>> get_elements(name=['FS1_B?*D266?', 'LS1_B*DCV*'],
        >>>              type=['BPM', 'QUAD'], srange=(154, 155))
        [FS1_BMS:QH_D2666 [QUAD] @ sb=154.144690]

        Note
        ----
        Select subsection by ``srange`` parameter is realized by new approach,
        other than ``~phantasy.library.Lattice.getLine()``, e.g. the result of
        ``getLine((10,11))`` contains element before the start range: i.e.
        ``LS1_WA03:PM_D1223:PM @ sb=9.929284``, which is beyond the range.

        See Also
        --------
        :func:`get_virtual_elements`
            Get virtual elements.
        :func:`next_elements`
            Get neighborhood of reference element.
        :class:`~phantasy.library.lattice.element.CaElement`
            Element class.
        """
        valid_types = self.get_all_types(virtual=False)

        # name
        if isinstance(name, basestring):
            ele_names = self._get_element_list(name)
        elif isinstance(name, (list, tuple)):
            ele_names = flatten(self._get_element_list(n) for n in name)
        else:
            ele_names = []

        # group
        if type is not None:
            if isinstance(type, basestring):
                type = type,
            _type_list = flatten(pattern_filter(valid_types, p) for p in type)
            ele_types = flatten(self._get_element_list(t) for t in _type_list)
        else:
            ele_types = []

        # srange
        if isinstance(srange, (list, tuple)):
            pos_start, pos_end = srange[0], srange[1]
            # by default elems is sorted, if not, sort it before using.
            elems = self._get_element_list('*', virtual=False)
            s = [e.sb for e in elems]
            index0 = bisect_index(s, pos_start)
            index1 = bisect_index(s, pos_end)
            ele_srange = elems[index0:index1]
        else:
            ele_srange = []

        ret_elems = get_intersection(ele_names, ele_types, ele_srange)

        sk = kws.get('sort_key', 'sb')
        if sk == 'pos':
            sk = 'sb'
        return sorted([e for e in ret_elems if not e.virtual],
                      key=lambda e: getattr(e, sk))

    def next_elements(self, ref_elem, count=1, **kws):
        """Get elements w.r.t reference element, according to the defined
        confinement.

        Parameters
        ----------
        ref_elem :
            ``CaElement`` object, reference element.
        count : int
            Skip element number after *ref_elem*, negative input means before,
            e.g. ``count=1`` will locate the next one of *ref_elem* in the
            investigated lattice, if keyword parameter *type* is given, will
            locate the next one element of the defined type; ``count=-1`` will
            locate in the opposite direction.

        Keyword Arguments
        -----------------
        type : str or list(str)
            (List of) Element type/group/family, if *type* is a list of more
            than one element types, the *next* parameter will apply on each
            type.
        range : str
            String of format ``start:stop:step``, to slicing the output list,
            e.g. return 50 BPMs after *ref_elem* (``count=50``), but only get
            every two elements, simply by setting ``range=0::2``.
        ref_include : True or False
            Include *ref_elem* in the returned list or not, False by default.

        Returns
        -------
        ret : List
            List of next located elements, ascendingly sorted by position, by
            default, only return one element (for eath *type*) that meets the
            confinement, return more by assgining *range* keyword parameter.

        Examples
        --------
        1. Select an element as reference element:

        >>> print(all_e)
        [LS1_CA01:CAV1_D1127 [CAV] @ sb=0.207064,
         LS1_CA01:BPM_D1129 [BPM] @ sb=0.511327,
         LS1_CA01:SOL1_D1131 [SOL] @ sb=0.643330,
         LS1_CA01:DCV_D1131 [VCOR] @ sb=0.743330,
         LS1_CA01:DCH_D1131 [HCOR] @ sb=0.743330,
         LS1_CA01:CAV2_D1135 [CAV] @ sb=0.986724,
         LS1_CA01:CAV3_D1143 [CAV] @ sb=1.766370,
         LS1_CA01:BPM_D1144 [BPM] @ sb=2.070634,
         LS1_CA01:SOL2_D1147 [SOL] @ sb=2.202637,
         LS1_CA01:DCV_D1147 [VCOR] @ sb=2.302637,
         LS1_CA01:DCH_D1147 [HCOR] @ sb=2.302637,
         LS1_CA01:CAV4_D1150 [CAV] @ sb=2.546031,
         LS1_WA01:BPM_D1155 [BPM] @ sb=3.109095,
         LS1_CA02:CAV1_D1161 [CAV] @ sb=3.580158,
         LS1_CA02:BPM_D1163 [BPM] @ sb=3.884422,
         LS1_CA02:SOL1_D1165 [SOL] @ sb=4.016425,
         LS1_CA02:DCV_D1165 [VCOR] @ sb=4.116425,
         LS1_CA02:DCH_D1165 [HCOR] @ sb=4.116425,
         LS1_CA02:CAV2_D1169 [CAV] @ sb=4.359819,
         LS1_CA02:CAV3_D1176 [CAV] @ sb=5.139465,
         LS1_CA02:BPM_D1178 [BPM] @ sb=5.443728]
        >>> ref_elem = all_e[5]

        2. Get next element of *ref_elem*:

        >>> lat.next_elements(ref_elem)
        [LS1_CA01:CAV3_D1143 [CAV] @ sb=1.766370]

        3. Get last of the next two element:

        >>> lat.next_elements(ref_elem, count=2)
        [LS1_CA01:BPM_D1144 [BPM] @ sb=2.070634]

        4. Get all of the next two elements:

        >>> lat.next_elements(ref_elem, count=2, range='0::1')
        [LS1_CA01:CAV3_D1143 [CAV] @ sb=1.766370,
         LS1_CA01:BPM_D1144 [BPM] @ sb=2.070634]

        5. Get all of the two elements before *ref_elem*:

        >>> lat.next_elements(ref_elem, count=-2, range='0::1')
        [LS1_CA01:DCV_D1131 [VCOR] @ sb=0.743330,
         LS1_CA01:DCH_D1131 [HCOR] @ sb=0.743330]

        6. Get next two BPM elements after *ref_elem*, including itself:

        >>> lat.next_elements(ref_elem, count=2, type=['BPM'],
        >>>                   ref_include=True, range='0::1')
        [LS1_CA01:CAV2_D1135:CAV @ sb=0.986724,
         LS1_CA01:BPM_D1144 [BPM] @ sb=2.070634,
         LS1_WA01:BPM_D1155 [BPM] @ sb=3.109095]

        7. Get with hybrid types:

        >>> lat.next_elements(ref_elem, count=2, type=['BPM', 'CAV'],
        >>>                   range='0::1')
        [LS1_CA01:CAV3_D1143 [CAV] @ sb=1.766370,
         LS1_CA01:BPM_D1144 [BPM] @ sb=2.070634,
         LS1_CA01:CAV4_D1150 [CAV] @ sb=2.546031,
         LS1_WA01:BPM_D1155 [BPM] @ sb=3.109095]
        """
        ref_include_flag = kws.get('ref_include', False)
        if not isinstance(ref_elem, CaElement):
            _LOGGER.warning("{} is not a valid CaElement.".format(str(ref_elem)))
            if ref_include_flag:
                return [ref_elem]
            else:
                return []

        if count == 0:
            return [ref_elem]

        count_is_positive = True if count > 0 else False
        if count_is_positive:
            eslice = kws.get('range', '-1::1')
        else:
            eslice = kws.get('range', '0:1:1')
        slice_tuple = [int(i) if i != '' else None for i in eslice.split(':')]
        eslice = slice(*slice_tuple)

        etype = kws.get('type', None)

        elem_sorted = sorted([e for e in self._elements if e.virtual == 0],
                             key=lambda e: e.sb)
        spos_list = [e.sb for e in elem_sorted]
        ref_idx = spos_list.index(ref_elem.sb)
        if count_is_positive:
            eslice0 = slice(ref_idx + 1, ref_idx + count + 1, 1)
        else:
            eslice0 = slice(ref_idx + count, ref_idx, 1)

        if etype is None:
            ret = elem_sorted[eslice0][eslice]
        else:
            if isinstance(etype, basestring):
                etype = etype,
            if count_is_positive:
                ret = flatten([e for e in elem_sorted[ref_idx + 1:]
                               if e.family == t][:count]
                              for t in etype)
            else:
                ret = flatten([e for e in elem_sorted[:ref_idx]
                               if e.family == t][count:]
                              for t in etype)
        if ref_include_flag:
            ret.append(ref_elem)
        return sorted(ret, key=lambda e: e.sb)

    def get_all_types(self, virtual=False, **kws):
        """Get names of element types (groups/families).

        Parameters
        ----------
        virtual : True or False
            Return virtual group or not, ``False`` by default.

        Returns
        -------
        ret : List(str)
            List of type names.

        See Also
        --------
        lattice_names : Names of all loaded lattices.
        get_all_names : Get all element names from given lattice.
        """
        all_groups = self.get_groups('*', empty=True)
        if virtual is True:
            return all_groups
        else:
            return [g for g in all_groups if g != 'HLA:VIRTUAL']

    def get_all_names(self, virtual=False, **kws):
        """Get names of all elements from  given lattice.

        Parameters
        ----------
        virtual : True or False
            Return virtual elements or not, ``False`` by default.

        Returns
        -------
        ret : List(str)
            List of element names.

        See Also
        --------
        lattice_names : Names of all loaded lattices.
        get_all_types : Get all element types from given lattice.
        """
        return [e.name for e in self._get_element_list('*', virtual=virtual)]

    def has_element(self, name):
        """If lattice has element or not.

        Parameters
        ----------
        name : str or CaElement
            Name of element or element itself.

        Returns
        -------
        ret : True or False
            True if lattice has element, or False.
        """
        if self._find_exact_element(name):
            return True
        else:
            return False

    def insert(self, elem, i=None, groups=None, **kws):
        """Ascendingly insert element regarding s-position, if *i* is defined,
        insert at *i*-th place.

        If *groups* is defined, add element into each group.

        Parameters
        ----------
        elem : str or CaElement
            CaElement object or element name.
        i : int
            Index to insert, append if None.
        groups : list or str
            Group name(s) the element belongs to.

        Keyword Arguments
        -----------------
        trust : True or False
            Trust input *elem* if True, else test first, False by default.

        See Also
        --------
        append : Add element at the end of lattice.
        :class:`~phantasy.library.lattice.CaElement`
        """
        if not kws.get('trust', False):
            elem = self._find_exact_element(elem)
            if elem is None:
                _LOGGER.warning("insert: not a valid element.")
                return

        if i is not None:
            self._elements.insert(i, elem)
        else:
            if len(self._elements) == 0:
                self._elements.append(elem)
            else:
                _inplace_order_insert(elem, self._elements)

        if isinstance(groups, basestring):
            groups = groups,
        if groups is not None:
            for g in groups:
                if g in self._group:
                    self._group[g].append(elem)
                else:
                    self._group[g] = [elem]

    def append(self, elem):
        """Append new element to lattice.

        Parameters
        ----------
        elem : CaElement
            Element object.
        """
        if not self.has_element(elem.name):
            self._elements.append(elem)

    def sort(self, elements=None, **kws):
        """Return sorted list of elements with defined key.

        Parameters
        ----------
        elements : List
            List of elements, could be returned from
            func:`~phantasy.library.lattice.Lattice.get_elements`, if not
            defined, entire lattice will be sorted.

        Keyword Arguments
        -----------------
        sort_key : str
            Ascendingly sort key for element list, ``name`` or ``pos``,
            ``pos`` by default, or other attributes valid for ``CaElement``.
        inplace : True or False
            If *inplace* is True, the original element list will be replaced
            with sorted one, False by default.

        Warning
        -------
        Inplace sort only supports the case of ``elements=None``.

        Returns
        -------
        ret : List
            Sorted list of elements.
        """
        if elements is None:
            elem0 = self._elements
        else:
            elem0 = elements
        if not isinstance(elem0, list):
            _LOGGER.warning("'elements' is not a list.")
            return []

        sk = kws.get('sort_key', 'sb')
        if sk == 'pos':
            sk = 'sb'
        sorted_elemlist = sorted([em for em in elem0],
                                 key=lambda e: getattr(e, sk))

        if kws.get('inplace', False):
            if elements is None:
                self._elements = sorted_elemlist
            else:
                _LOGGER.warning(
                    "'inplace' sort is only valid when 'elements=None'."
                )

        return sorted_elemlist

    def size(self):
        """Total number of elements."""
        return len(self._elements)

    def remove(self, name):
        """Remove element with *name*, or return None.

        Parameters
        ----------
        name : str
            Name of element.

        Returns
        -------
        ret :
            Element if success or None.
        """
        for i, e in enumerate(self._elements):
            if e.name != name:
                continue
            return self._elements.pop(i)
        return None

    def update_groups(self):
        """Update group attribute by iterating over all elements.

        Returns
        -------
        ret : dict
            Dict of groups, with group names as keys and group members as
            values.
        """
        for e in self._elements:
            for g in e.group:
                g_lst = self._group.setdefault(g, [])
                if e not in g_lst:
                    g_lst.append(e)

    def add_group(self, name):
        """Create a new group.

        Parameters
        ----------
        name : str
            Group name.
        """
        if name not in self._group:
            self._group[name] = []
        else:
            raise ValueError("Group '{}' exists.".format(name))

    def remove_group(self, name, **kws):
        """Remove group defined by *name*, by default only remove empty group.

        Parameters
        ----------
        name : str
            Group name.

        Keyword Arguments
        -----------------
        empty_only: True or False
            Remove empty group only if True, True by default.
        """
        if name not in self._group:
            raise ValueError("Group '{}' does not exist.".format(name))

        empty_only = kws.get('empty_only', True)
        if len(self._group[name]) > 0:
            if empty_only:
                raise ValueError("Cannot remove non-empty group '{}'.".format(
                    name))
            else:
                print("Warning: Group to remove is not empty.")
        self._group.pop(name)

    def add_group_member(self, group, member, **kws):
        """Add a *member* to *group*, if *group* is new, add and update
        *member* group only when *new* if True.

        Parameters
        ----------
        group : str
            Group name.
        member :
            CaElement.

        Keyword Arguments
        -----------------
        new : True or False
            If *group* is new, add and update when *new* is True, or ignore.
        """
        new = kws.get('new', True)
        elem = self._find_exact_element(member)
        if elem is None:
            raise ValueError("Invalid element '{}'.".format(member))

        if group in self._group:
            if elem in self._group[group]:
                msg = "'{0}' is already in group: '{1}'.".format(
                    elem.name, group)
                print("Warning: {0}".format(msg))
                _LOGGER.warning(msg)
                return
            else:
                elem.group.add(group)
                _inplace_order_insert(elem, self._group[group])
                msg = "Add '{0}' into group '{1}'.".format(
                    elem.name, group)
                _LOGGER.info(msg)
        elif new:
            self._group[group] = [elem]
            elem.group.add(group)
            msg = "Add '{0}' into new group '{1}'.".format(
                elem.name, group)
            _LOGGER.info(msg)
        else:
            raise ValueError(
                "Group {} does not exist, use 'new=True' to add it.".format(
                    group))

    def has_group(self, name):
        """Check if group exists or not.

        Parameters
        ----------
        name : str
            Group name.

        Returns
        -------
        ret : True or False
            True if has group *name* or False.
        """
        return name in self._group

    def remove_group_member(self, group, member):
        """Remove a *member* from *group*.

        Parameters
        ----------
        group : str
            Group name.
        member :
            CaElement.
        """
        if group not in self._group:
            raise ValueError(
                "Remove error: group '{}' does not exist.".format(group))
        if member in self._group[group]:
            self._group[group].remove(member)
        else:
            raise ValueError(
                "Remove error: '{}' not in group '{}'.".format(
                    member, group))

    def get_groups(self, name=None, element=None, **kws):
        """Get groups filtered by *name*, if *element* is given, a list of
        groups that *element* belongs to would return.

        Parameters
        ----------
        name : str
            Group name string, could be Unix shell style pattern.
        element : str
            Element name.

        Keyword Arguments
        -----------------
        empty : True or False
            If *empty* is True, also return name the empty groups, else not,
            True by default.

        Returns
        -------
        ret : list
            List of group names.
        """
        if element is None:
            if kws.get('empty', True):
                g = [k for k, v in self._group.items() if fnmatch(k, name)]
            else:
                g = [k for k, v in self._group.items() if fnmatch(k, name)
                     and v != []]
            return g
        else:
            return [k for k, v in self._group.items()
                    if fnmatch(k, name) and element in [el.name for el in v]]

    def get_group_members(self, group, **kws):
        """Return element members by applying proper filtering operation on
        each group from *group*, filtering operation could be defined by
        keyword argument *op*.

        Parameters
        ----------
        group: str or list
            Group name string or list[str], could be Unix shell style pattern.

        Keyword Arguments
        -----------------
        op : str
            Valid options: ``and``, ``or``.

        Returns
        -------
        ret : list
            List of elements.
        """
        op = kws.get('op', 'and')
        if isinstance(group, basestring):
            group = group,
        group_list = flatten(
            [[g for g in self._group if fnmatch(g, gi)] for gi in group]
        )
        elem_dict = {g: self._group[g] for g in group_list}

        if op == 'and':
            return get_intersection(**elem_dict)
        else:  # op = 'or'
            return list(set(flatten(elem_dict.values())))

    @property
    def orm(self):
        """Array: Orbit response matrix.

        See Also
        --------
        :func:`~phantasy.library.physics.orm.get_orm`
            Calculator orbit response matrix.
        """
        return self._orm

    @orm.setter
    def orm(self, m):
        self._orm = m

    def correct_orbit(self, correctors, bpms, **kws):
        """Correct orbit by using ORM.

        Parameters
        ----------
        correctors : list
            List of corrector elements.
        bpms : list
            List of BPM elements.

        Keyword Arguments
        -----------------
        cor_field : str
            Field name for correctors, ``'ANG'`` by default.
        orb_field : tuple[str]
            Field names for monitors to retrieve orbit data, ``('X', 'Y')`` for
            *x* and *y* directions by default.
        xoy : str
            'x'('y') for monitoring 'x'('y') direction,'xy' for both (default).
        damping_factor : float
            Factor to correct orbit, default is 0.05, which would decrease beam
            orbit (BPM readings) by 5% for every correction.
        iteration : int
            Iteration numbers of correction, default is 1.
        wait : float
            Wait time after set value, in *sec*, 1.0 by default.

        Returns
        -------
        """
        itern = kws.get('iteration', 1)
        cor_field = kws.get('cor_field', 'ANG')
        damp_fac = kws.get('damping_factor', 0.05)
        wait = kws.get('wait', 1.0)

        if self._orm is None:
            _LOGGER.error("correct_orbit: ORM is not available, set ORM first.")
            raise RuntimeError("INVALID ORM data.")
        m = self._orm
        m_inv = inverse_matrix(m)

        n_cor = len(correctors)
        for i in range(1, itern + 1):
            bpm_readings = get_orbit(bpms, **kws)
            delt_cor = np.dot(m_inv, -bpm_readings * damp_fac)
            for ic, (e, v) in enumerate(zip(correctors, delt_cor)):
                print(
                    "Correct cor[{0:>2d}/{1:>2d}]: {2:<20s} with {3:>10.4e} mrad.".format(
                        ic + 1, n_cor, e.name, v * 1e3))
                v0 = getattr(e, cor_field)
                setattr(e, cor_field, v0 + v)
                time.sleep(wait)
            next_iter = r_input(
                "Continue correction iteration: {0}/{1}? ([Y]/N)".format(i + 1,
                                                                         itern)
            )
            if next_iter.upper() in ['Y', '']:
                continue
            else:
                break

    def measure_orm(self):
        pass

    ###############################################################################

    def _find_element_s(self, s, eps=1e-9, loc='left'):
        """Given s location, find an element at this location, mostly return
        the element index mostly near s, by left/right approaching.

        If this is drift space, find the element at 'left' or 'right' of the
        given point.
        """
        if loc not in ['left', 'right']:
            raise ValueError('loc must be in ["left", "right"]')

        # normalize s into [0, C]
        sn = s
        if s > self.length:
            sn = s - self.length
        if s < 0:
            sn = s + self.length

        if sn < 0 or sn > self.length:
            raise ValueError("s= %f out of boundary ([%f, %f])"
                             % (s, -self.length, self.length))
        ileft, eleft = -1, self.length
        iright, eright = -1, self.length
        for i, e in enumerate(self._elements):
            if e.virtual > 0:
                continue
            # assuming elements is in order
            if abs(e.sb - s) <= eleft:
                ileft, eleft = i, abs(e.sb - s)
            if abs(e.se - s) <= eright:
                iright, eright = i, abs(e.se - s)
        if loc == 'left':
            return ileft
        elif loc == 'right':
            return iright

    def createLatticeModelMap(self, mapfile):
        """Create a mapping between lattice layout and model output from a file

        :param mapfile: file name which has mapping information.

        """
        mapping = np.loadtxt(mapfile, dtype=str)
        if self.latticemodelmap is not None:
            self.latticemodelmap.clear()
        else:
            self.latticemodelmap = {}
        for idx, mp in enumerate(mapping):
            if mp[0] == "NONE":
                continue
            if mp[0] not in self.latticemodelmap:
                self.latticemodelmap[mp[0]] = {}
            if mp[1] not in self.latticemodelmap[mp[0]]:
                self.latticemodelmap[mp[0]][mp[1]] = []
            self.latticemodelmap[mp[0]][mp[1]].append(idx)

    def getOverlapped(self):
        ret = []
        i = 0
        while i < len(self._elements):
            # for each element, searching the elements behind it
            j = i + 1
            ov = []
            while j < len(self._elements):
                if self._elements[j].sb < self._elements[i].se:
                    ov.append(self._elements[j].name)
                elif self._elements[j].sb >= self._elements[i].se:
                    break
                j = j + 1
            if ov:
                ret.append([self._elements[i].name] + ov)
            i = i + 1
        if ret:
            return ret
        else:
            return None

    def save(self, fname, dbmode='c'):
        """save the lattice into binary data, using writing *dbmode*.

        see also Python Standard Lib `shelve`
        """
        f = shelve.open(fname, dbmode)
        pref = "lat.%s." % self.mode
        f[pref + 'group'] = self._group
        f[pref + 'elements'] = self._elements
        f[pref + 'mode'] = self.mode
        f[pref + "source"] = self.source
        f[pref + 'tune'] = self.tune
        f[pref + 'chromaticity'] = self.chromaticity
        f.close()

    def load(self, fname):
        """load the lattice from binary data

        In the db file, all lattice has a key with prefix 'lat.mode.'. If the
        given mode is empty string, then use 'lat.'
 
        seealso Python Standard Lib `shelve`
        """
        f = shelve.open(fname, 'r')
        pref = "lat."
        self._group = f[pref + 'group']
        self._elements = f[pref + 'elements']
        self.mode = f[pref + 'mode']
        self.source = f[pref + "source"]
        self.tune = f[pref + 'tune']
        self.chromaticity = f[pref + 'chromaticity']
        if self._elements:
            self.length = self._elements[-1].se
        f.close()

    def mergeGroups(self, parent, children):
        """merge child group(s) into a parent group

        the new parent group is replaced by this new merge of children
        groups. no duplicate element will appears in merged *parent* group
        
        Examples
        ---------
        >>> mergeGroups('BPM', ['BPMX', 'BPMY'])
        >>> mergeGroups('TRIM', ['TRIMX', 'TRIMY'])
        >>> mergeGroups('BPM', ['BPM', 'UBPM'])

        """
        if isinstance(children, str):
            chlist = [children]
        elif hasattr(children, '__iter__'):
            chlist = children[:]
        else:
            raise ValueError("children can be string or list of string")

        # if not self._group.has_key(parent):
        pl = []

        for child in chlist:
            if child not in self._group:
                _LOGGER.warning("WARNING: no %s group found" % child)
                continue
            for elem in self._group[child]:
                if elem in pl:
                    continue
                pl.append(elem)
        self._group[parent] = pl

    def getLocations(self, elemsname):
        """
        if elems is a string(element name), do exact match and return
        single number.  if elems is a list do exact match on each of them,
        return a list. None if the element in this list is not found.

        .. warning::
        
          If there are duplicate elements in *elems*, only first
          appearance has location returned.

        :Example:

          >>> getLocations(['BPM1', 'BPM1', 'BPM1']) #doctest: +SKIP
          [0.1, None, None]

        """

        if isinstance(elemsname, str):
            e = self._find_exact_element(elemsname)
            return e.sb
        elif isinstance(elemsname, list):
            ret = [None] * len(elemsname)
            for elem in self._elements:
                if elem.name in elemsname:
                    idx = elemsname.index(elem.name)
                    ret[idx] = elem.s
            return ret
        else:
            raise ValueError("not recognized type of *elems*")

    def getLocationRange(self):
        s0, s1 = 0.0, 1.0
        for elem in self._elements:
            if elem.virtual:
                continue
            if isinstance(elem.sb, (int, float)):
                s0 = elem.sb
                break
        for i in range(1, 1 + len(self._elements)):
            elem = self._elements[-i]
            if elem.virtual:
                continue
            if isinstance(elem.se, (int, float)) and elem.se > s0:
                s1 = elem.se
                break
        return s0, s1

    def _get_element_list(self, group, **kwargs):
        """Get a list of element objects.

        Parameters
        ----------
        group : str, list.
            Element name, pattern or name list.
            when it is str, searching for elements of defined group name;
            if not found, searching for a group with name *group*.
            At last treat it as a pattern to match the element names.
            When the input *group* is a list, each string in this list will
            be treated as exact string instead of pattern.

        Keyword Arguments
        -----------------
        virtual : bool
            Including virtual element or not, False by default.

        Returns
        --------
        ret : list
            List of element objects.
        """
        virtual = kwargs.get('virtual', False)
        # do exact element name match first
        elem = self._find_exact_element(group)
        if elem is not None:
            return [elem]

        # do exact group name match
        if group in self._group:
            return self._group[group][:]

        if isinstance(group, basestring):
            # do pattern match on element name
            ret, names = [], []
            for e in self._elements:
                if e.name in names:
                    continue
                if not virtual and e.virtual:
                    continue
                if fnmatch(e.name, group):
                    ret.append(e)
                    names.append(e.name)
            return ret
        elif isinstance(group, list):
            # exact one-by-one match, None if not found
            return [self._find_exact_element(e) for e in group]

    def _matchElementCgs(self, elem, **kwargs):
        """check properties of an element
        
        - *cell*
        - *girder*
        - *symmetry*
        """

        cell = kwargs.get("cell", None)

        if isinstance(cell, str) and elem.cell != cell:
            return False
        elif hasattr(cell, "__iter__") and not elem.cell in cell:
            return False

        girder = kwargs.get("girder", None)

        if isinstance(girder, str) and elem.girder != girder:
            return False
        elif hasattr(girder, "__iter__") and not elem.girder in girder:
            return False

        symmetry = kwargs.get("symmetry", None)

        if isinstance(symmetry, str) and elem.symmetry != symmetry:
            return False
        elif hasattr(symmetry, "__iter__") and not elem.symmetry in symmetry:
            return False

        return True

    def _getElementsCgs(self, group='*', **kwargs):
        """
        call signature::
        
          getElementsCgs(group)

        Get a list of elements from cell, girder and sequence

        - *cell*
        - *girder*
        - *symmetry*

        :Example:

            >>> getElementsCgs('BPMX', cell=['C20'], girder=['G2'])

        When given a general group name, check the following:

        - element name
        - element family
        - existing *group*: 'BPM', 'BPMX', 'BPMY', 'A', 'C02', 'G4'

            - cell
            - girder
            - symmetry
        """

        # return empty set if not specified the group
        if not group: return None

        elem = []
        for e in self._elements:
            # skip for duplicate
            if e.name in elem: continue

            if not self._matchElementCgs(e, **kwargs):
                continue

            if e.name in self._group.get(group, []):
                elem.append(e.name)
            elif fnmatch(e.name, group):
                elem.append(e.name)
            else:
                pass

                # if cell and not e.cell in cell: continue
                # if girder and not e.girder in girder: continue
                # if symmetry and not e.symmetry in symmetry: continue

        return elem

    def getNeighbors(self, elemname, groups, n, elemself=True):
        """
        Assuming self._elements is in s order

        the element matched with input 'element' string should be unique
        and exact.

        If the input *element* name is also in one of the *groups*, no
        duplicate the result.
        
        For a linear machine, it will fill `None` is there is no enough elements in upstream or in downstream. 

        :Example:

            >>> getNeighbors('P4', 'BPM', 2)
            ['P2', 'P3', 'P4', 'P5', 'P6']
            >>> getNeighbors('Q3', 'BPM', 2)
            ['P2', 'P3', 'Q3', 'P4', 'P5']
            >>> getNeighbors('Q3', ["BPM", "SEXT"], 2)
        """

        e0 = self._find_exact_element(elemname)
        if not e0:
            raise ValueError("element %s does not exist" % elemname)

        el = []
        if isinstance(groups, basestring):
            el = self._get_element_list(groups, virtual=0)
        elif isinstance(groups, (list, tuple)):
            el = self.getGroupMembers(groups, op="union")

        if not el:
            raise ValueError("elements/group %s does not exist" % groups)
        if e0 in el:
            el.remove(e0)

        i0 = len(el)
        for i, e in enumerate(el):
            if e.sb < e0.sb:
                continue
            i0 = i
            break
        ret = [e0] if elemself else []
        for i in range(n):
            _, r = divmod(i0 - i - 1, len(el))
            if self.isring or el[r].sb < e0.sb:
                # insert into the front no matter what for a ring  
                # or when the position is smaller than that of current element for a linear machine
                ret.insert(0, el[r])
            else:
                ret.insert(0, None)
            _, r = divmod(i0 + i, len(el))
            if self.isring or el[r].sb > e0.sb:
                # append into the list no matter what for a ring  
                # or when the position is larger than that of current element for a linear machine
                ret.append(el[r])
            else:
                ret.append(None)
        return ret

    def getClosest(self, elemname, groups):
        """
        Assuming self._elements is in s order

        the element matched with input 'element' string should be unique
        and exact.

        :Example:

            >>> getClosest('P4', 'BPM')
            >>> getClosest('Q3', 'BPM')
            >>> getClosest('Q3', ["QUAD", "SEXT"])

        The result can not be virtual element.
        """

        e0 = self._find_exact_element(elemname)
        if not e0:
            raise ValueError("element %s does not exist" % elemname)

        el = []
        if isinstance(groups, basestring):
            el = self._get_element_list(groups, virtual=0)
        elif isinstance(groups, (list, tuple)):
            el = self.getGroupMembers(groups, op="union")

        if not el: raise ValueError("elements/group %s does not exist" % groups)

        idx, ds = 0, el[-1].sb
        for i, e in enumerate(el):
            if e == e0: continue
            if isinstance(e.sb, (list, tuple)):
                ds0 = abs(e.sb[0] - e0.sb)
            else:
                ds0 = abs(e.sb - e0.sb)
            if ds0 > ds: continue
            idx = i
            ds = ds0

        return el[idx]

    def __repr__(self):
        s0 = "#Name of segment: '{}', unit: [m]".format(self.name)
        s1 = '#{0:<4s}{1:^20s} {2:<6s} {3:>10s} {4:>10s}'.format(
            'IDX', 'NAME', 'FAMILY', 'POSITION', 'LENGTH'
        )
        ret = [s0, s1]

        fmt = "{{idx:<{wi}d}} {{name:<{wn}s}} {{family:<{wf}s}} {{pos:>10.4f}} {{len:>10.4f}}".format(
            wi=4, wn=20, wf=6)
        for i, e in enumerate(self._elements):
            if e.virtual:
                continue
            ret.append(fmt.format(idx=i, name=e.name, family=e.family,
                                  pos=e.sb, len=e.length))
        return '\n'.join(ret)


def _inplace_order_insert(elem, lat):
    k = 0
    for ielem in lat:
        if ielem.sb < elem.sb:
            k += 1
            continue
        else:
            break
    lat.insert(k, elem)


def _normalize_phase(x):
    while x >= 360.0:
        x -= 360.0
    while x < 0.0:
        x += 360.0
    return x


def _is_viewer(elem):
    """Test if elem is viewer, e.g. BPM, PM, ...
    """
    return elem.family in ['BPM']


def _get_retroactive_trace_history(trace_history_data, retroaction):
    data = trace_history_data
    if isinstance(retroaction, (float, int, long)):
        # absolute time
        retval = [_entry for _entry in data
                  if _entry['timestamp'] >= retroaction]
    else:
        # relative time
        retro_datetime = parse_dt(retroaction, datetime.now(), epoch=True)
        retval = [_entry for _entry in data
                  if _entry['timestamp'] >= retro_datetime]
    return retval


def _get_control_field(elem, field):
    """Get field value(s) from element, source is control environment.
    """
    if not isinstance(field, (list, tuple)):
        field = field,
    return {f: getattr(elem, f) for f in field}
