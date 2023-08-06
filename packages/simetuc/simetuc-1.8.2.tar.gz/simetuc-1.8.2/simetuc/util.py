# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 16:45:32 2016

@author: Pedro
"""

#import sys
import tempfile
from contextlib import contextmanager
import os
from collections import namedtuple
import logging
import itertools
import warnings
from functools import wraps
import numpy as np

from enum import Enum
from typing import Generator, Sequence, Callable, Any, Tuple, Dict, List, Union, Optional


# http://stackoverflow.com/a/11892712
@contextmanager
def temp_config_filename(data: str) -> Generator:
    '''Creates a temporary file and writes text data to it. It returns its filename.
        It deletes the file after use in a context manager.
    '''
    # file won't be deleted after closing
    temp = tempfile.NamedTemporaryFile(mode='wt', delete=False)
    temp.write(data)
    temp.close()
    yield temp.name
    os.unlink(temp.name)  # delete file


@contextmanager
def temp_bin_filename() -> Generator:
    '''Creates a temporary binary file. It returns its filename.
        It deletes the file after use in a context manager.
    '''
    # file won't be deleted after closing
    temp = tempfile.NamedTemporaryFile(mode='wb', delete=False)
    temp.close()
    yield temp.name
    os.unlink(temp.name)  # delete file


class cached_property():
    '''Computes attribute value and caches it in the instance.
    Python Cookbook (Denis Otkidach) http://stackoverflow.com/users/168352/denis-otkidach
    This decorator allows you to create a property which can be computed once and
    accessed many times. Sort of like memoization.
    http://stackoverflow.com/a/6429334
    '''
    def __init__(self, method: Callable, name: Optional[str] = None) -> None:
        '''Record the unbound-method and the name'''
        self.method = method
        self.name = name or method.__name__
        self.__doc__ = method.__doc__

    def __get__(self, inst: object, cls: type) -> Any:
        '''self: <__main__.cache object at 0xb781340c>
           inst: <__main__.Foo object at 0xb781348c>
           cls: <class '__main__.Foo'>
        '''
        if inst is None:
            # instance attribute accessed on class, return self
            # You get here if you write `Foo.bar`
            return self
        # compute, cache and return the instance's attribute value
        result = self.method(inst)
        # setattr redefines the instance's attribute so this doesn't get called again
        setattr(inst, self.name, result)
        return result


# namedtuple for the concentration of solutions
Conc = namedtuple('Concentration', ['S_conc', 'A_conc'])


class IonType(Enum):
    '''Type of ion: sensitizer or activator'''
    sensitizer = 0
    activator = 1
    S = sensitizer
    A = activator


class Transition():
    '''Base class for all transitions from an initial to a final state in a ion.'''
    def __init__(self, ion: IonType, state_i: int, state_f: int,
                 label_ion: str = '', label_i: str = '', label_f: str = '') -> None:
        self.ion = ion
        self.state_i = state_i
        self.state_f = state_f

        self.label_ion = label_ion
        self.label_i = label_i
        self.label_f = label_f

        self.repr_ion = self.label_ion if self.label_ion else self.ion.name[0].upper()
        self.repr_state_i = self.label_i if self.label_i else self.state_i
        self.repr_state_f = self.label_f if self.label_f else self.state_f

#        self.name = '{} -> {}'.format(self.repr_state_i, self.repr_state_f)

    def __repr__(self) -> str:
        return '{}({}: {}->{})'.format(self.__class__.__name__, self.repr_ion,
                                       self.repr_state_i, self.repr_state_f)

    def __eq__(self, other: object) -> Union[bool, Any]:
        '''Two Transitions are equal if all their attributes are equal.'''
        if not isinstance(other, Transition):
            return NotImplemented
        for attr in ['ion', 'state_i', 'state_f']:
            if getattr(self, attr) != getattr(other, attr):
                return False
        return True

    def __ne__(self, other: object) -> bool:
        '''Not equal operator'''
        return not (self == other)

    def __hash__(self) -> int:
        '''Hash the ion, and initial and final states'''
        return hash((self.ion, self.state_i, self.state_f))


class DecayTransition(Transition):
    '''Decay or branching ratio transition.'''
    def __init__(self, ion: IonType, state_i: int, state_f: int,
                 decay_rate: Optional[float] = None, branching_ratio: Optional[float] = None,
                 label_ion: str = '', label_i: str = '', label_f: str = '') -> None:
        super(DecayTransition, self).__init__(ion, state_i, state_f, label_ion, label_i, label_f)
        self.decay_rate = decay_rate
        self.branching_ratio = branching_ratio

        if decay_rate is not None:
            self.name = 'k_{}{}'.format(state_i, state_f)
        elif branching_ratio is not None:
            self.name = 'B_{}{}'.format(state_i, state_f)
        else:
            raise ValueError('Either the decay rate or the branching ratio must be given.')

    def __repr__(self) -> str:
        base_repr = super(DecayTransition, self).__repr__()
        if self.decay_rate is not None:
            info = ', k={:.2e}'.format(self.decay_rate)
        elif self.branching_ratio is not None:
            info = ', B={:.3f}'.format(self.branching_ratio)
        else:
            info = ''
        return base_repr.replace(')', '') + '{})'.format(info)

    def __eq__(self, other: object) -> Union[bool, Any]:
        '''Comparing DecayTransitions checks all attributes.
            Comparing to a Transition only checks the common attributes.'''
        # comparing DecayTransitions checks all attributes
        if isinstance(other, DecayTransition):
            base_eq = super(DecayTransition, self).__eq__(other)
            if base_eq is False:
                return False
            for attr in ['decay_rate', 'branching_ratio']:
                if getattr(self, attr) != getattr(other, attr):
                    return False
            return True
        # comparing to a Transition only checks the common attributes
        elif isinstance(other, Transition):
            return super(DecayTransition, self).__eq__(other)
        return NotImplemented

    def __ne__(self, other: object) -> bool:
        '''Not equal operator'''
        return not (self == other)

    def __hash__(self) -> int:
        '''Equal (Decay)Transitions have equal hash,
            different DecayTransitions may have the same hash too
            (if they only have different decay or branching ratios)'''
        return hash((self.ion, self.state_i, self.state_f))

    @property
    def value(self) -> Optional[float]:
        '''Returns the value associated with this DecayTransition'''
        if self.decay_rate is not None:
            return self.decay_rate  # pragma: no cover
        elif self.branching_ratio is not None:
            return self.branching_ratio
        else:
            return None


    @value.setter
    def value(self, value: float) -> None:
        '''Sets the value associated with this DecayTransition'''
        if self.decay_rate is not None:
            self.decay_rate = value  # pragma: no cover
        elif self.branching_ratio is not None:
            self.branching_ratio = value


class Excitation():
    '''Excitation transition, with all the parameters.'''
    def __init__(self, ion: IonType, state_i: int, state_f: int,
                 active: bool, degeneracy: float, pump_rate: float,
                 power_dens: float, t_pulse: Optional[float] = None,
                 label_ion: str = '', label_i: str = '', label_f: str = '') -> None:
        self.transition = Transition(ion, state_i, state_f, label_ion, label_i, label_f)
        self.active = active
        self.degeneracy = degeneracy
        self.pump_rate = pump_rate
        self.power_dens = power_dens
        self.t_pulse = t_pulse

    def __repr__(self) -> str:
        base_repr = repr(self.transition).replace('Transition', 'Excitation')
        active = 'active' if self.active else 'inactive'
        return base_repr.replace(')', '') + ', {})'.format(active)

    def __eq__(self, other: object) -> Union[bool, Any]:
        '''Two settings are equal if all their attributes are equal.'''
        if not isinstance(other, Excitation):
            return NotImplemented
        for attr in ['transition', 'active', 'degeneracy', 'pump_rate', 'power_dens', 't_pulse']:
            if getattr(self, attr) != getattr(other, attr):
                return False
        return True

    def __ne__(self, other: object) -> bool:
        '''Not equal operator'''
        return not (self == other)


class EneryTransferProcess():
    '''Information about an energy transfer process'''
    def __init__(self, transitions: Sequence[Transition],
                 mult: int, strength: float, strength_avg: Optional[float] = None,
                 name: str = '') -> None:
        self.transitions = tuple(transitions)
        self.mult = int(mult)
        self.strength = strength
        self._strength_avg = strength_avg
        self.name = name

        # first the initial indices, then the final ones
        temp = [(trans.state_i, trans.state_f) for trans in transitions]
        self.indices = tuple(itertools.chain.from_iterable(zip(*temp)))
        self.type = tuple(trans.ion for trans in transitions)
        self.cooperative = True if len(transitions) == 3 else False

    def __repr__(self) -> str:
        init_states = '+'.join('{}({})'.format(trans.repr_ion, trans.repr_state_i)
                               for trans in self.transitions)
        final_states = '+'.join('{}({})'.format(trans.repr_ion, trans.repr_state_f)
                                for trans in self.transitions)
        return 'ETProcess({}->{}, n={:d}, C={:.2g})'.format(init_states, final_states,
                                                          self.mult, self.strength)

    def __eq__(self, other: object) -> Union[bool, Any]:
        '''Two ET processes are equal if all their attributes are equal.'''
        if not isinstance(other, EneryTransferProcess):
            return NotImplemented
        for attr in ['transitions', 'mult']:
            if getattr(self, attr) != getattr(other, attr):
                return False
        return True

    def __ne__(self, other: object) -> bool:
        '''Not equal operator'''
        return not (self == other)

#    def __hash__(self) -> int:
#        '''Hash only the transitions and multipolarity b/c these don't change'''
#        return hash((self.transitions, self.mult))

    @cached_property
    def strength_avg(self) -> float:
        '''Return the strength for average rate eqs. If it wasn't given when creating this ET
        process, it returns the normal strength.'''
        if self._strength_avg is not None:
            return self._strength_avg
        else:
            return self.strength

    @property
    def value(self) -> float:
        return self.strength

    @value.setter
    def value(self, val: float) -> None:
        self.strength = val


def log_exceptions_warnings(ignore_warns: Union[Callable, Warning,
                                                List[Warning], None] = None) -> Callable:
    '''Decorator to log exceptions and warnings'''
    if not isinstance(ignore_warns, List): ignore_warns = [ignore_warns]  # type: ignore
    def decorator(function: Callable) -> Callable:
        @wraps(function)
        def wrapper(*args: Tuple, **kwargs: Dict) -> Any:
            try:
                with warnings.catch_warnings(record=True) as warn_list:
                    # capture all warnings
                    warnings.simplefilter('always')
                    ret = function(*args, **kwargs)
            except Exception as exc:
                logger = logging.getLogger(function.__module__)
                logger.error(str(exc))
                raise
            for warn in warn_list:  # type: ignore
                if warn.category in ignore_warns: continue  # type: ignore
                logger = logging.getLogger(function.__module__)
                log_msg = (warn.category.__name__ + ': "' + str(warn.message) +
                           '" in ' + os.path.basename(warn.filename) +
                           ', line: ' + str(warn.lineno) + '.')
                logger.warning(log_msg)
                warn_msg = str(warn.message) + '.'
                # re-raise warnings
                # stacklevel=2 makes the warning refer to log_exceptions_warnings‘s caller,
                # rather than to the source of log_exceptions_warnings() itself
                warnings.warn(warn_msg, warn.category, stacklevel=2)
            return ret
        return wrapper
    if callable(ignore_warns[0]) and not hasattr(ignore_warns[0], 'with_traceback'): # decorator called without parenthesis
        return decorator(ignore_warns[0]) # return 'wrapper'
    else: # decorator called with parenthesis
        return decorator

class Blacklist(logging.Filter):
    def __init__(self, level: int, *blacklist: str) -> None:
        self.level = level
        self.blacklist = [logging.Filter(name) for name in blacklist]

    def filter(self, record: logging.LogRecord) -> bool:  # pragma: no cover
        if record.levelno >= self.level:
            return True
        return not any(f.filter(record) for f in self.blacklist)

@contextmanager
def disable_console_handler(logger_name: str, level: int = logging.WARNING) -> Generator:  # pragma: no cover
    '''Disable the console handler of the logger (for records lower than level).'''
    for handler in logging.getLogger().handlers:
        if isinstance(handler, logging.StreamHandler):
#            if handler.stream == sys.stdout:  # type: ignore
            filter = Blacklist(level, logger_name)
            handler.addFilter(filter)
            yield None
            handler.removeFilter(filter)
            return


@contextmanager
def disable_loggers(logger_name_lst: List[str], level: int = logging.INFO) -> Generator:  # pragma: no cover
    '''Temporary change the console handler level.'''
    levels = []
    for logger_name in logger_name_lst:
        logger = logging.getLogger(logger_name)
        levels.append(logger.getEffectiveLevel())
        logger.disabled = True
        logger.propagate = False
    yield None
    for logger_name, logger_level in zip(logger_name_lst, levels):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logger_level)
        logger.disabled = False
        logger.propagate = True
    return


def exp_to_10(float_number: float) -> str:
    '''Convert a float to str using power of ten notation instead of exp.
        ie: 3e5 -> 3×10^5'''
    exponent = np.floor(np.log10(float_number))
    mantissa = float_number/10**exponent
    mantissa_format = str(mantissa)[0:3]
    return "{}×10^{}".format(mantissa_format, str(int(exponent)))

class LabelError(ValueError):
    '''A label in the configuration file is not correct'''
    pass


class ConfigError(SyntaxError):
    '''Something in the configuration file is not correct'''
    pass


class ConfigWarning(UserWarning):
    '''Something in the configuration file is not correct'''
    pass


def save_file_full_name(lattice: dict, prefix: str = '') -> str:  # pragma: no cover
    '''Return the full name to save a file (without extention or prefix).'''
    path = os.path.join('results', lattice['name'])
    os.makedirs(path, exist_ok=True)
    filename = prefix + '_' + '{}uc_{}S_{}A'.format(int(lattice['N_uc']),
                                                    float(lattice['S_conc']),
                                                    float(lattice['A_conc']))
    return os.path.join(path, filename)
