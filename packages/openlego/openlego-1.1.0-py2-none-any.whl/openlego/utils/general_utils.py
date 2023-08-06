#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright 2018 D. de Vries

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

This file contains the definition of general utility functions.
"""
from __future__ import absolute_import, division, print_function

import re
import warnings

import numpy as np
from lxml import etree
from openmdao.core.driver import Driver
from typing import Callable, Any, Optional, Union, Type


def try_hard(fun, *args, **kwargs):
    # type: (Callable, *Any, **Any) -> Any
    """Try repeatedly to call a function until it returns successfully.

    Utility function that repeatedly tries to call a given function with the given arguments until that function
    successfully returns. It is possible to limit the maximum number of attempts by setting the try_hard_limit argument.


    Parameters
    ----------
        fun : function
            The function to try to call.

        *args
            Any ordered arguments to pass to the function.

        **kwargs
            Any named arguments to pass to the function.


    Returns
    -------
        any
            The return value of the function to be called.

    Notes
    -----
        This function is part of a workaround to deal with APIs crashing in a non-predictable manner, seemingly random
        way. It was found that, when simply trying to call such functions again, the problem seemed to not exist
        anymore.
    """
    warnings.simplefilter('always', UserWarning)
    try_hard_limit = -1
    if kwargs is not None:
        if 'try_hard_limit' in kwargs.keys():
            try_hard_limit = kwargs['try_hard_limit']
            del kwargs['try_hard_limit']

    msg = None
    return_value = None
    successful = False
    attempts = 0
    while not successful:
        try:
            return_value = fun(*args, **kwargs)
            successful = True
        except Exception as e:
            attempts += 1

            if msg is None:
                msg = 'Had to try again to evaluate: %s(' % fun.__name__ + ', '.join(['%s' % arg for arg in args])
                if kwargs is not None:
                    msg += ', '.join(['%s=%s' % (key, value) for key, value in kwargs.items()])
                msg += '). The following exception was raised: "%s"' % e.message

            if 0 < try_hard_limit <= attempts:
                raise
            else:
                warnings.warn(msg)

    return return_value


class CachedProperty(property):
    """Subclass of `property` using a cache to avoid recalculating an expensive `property` every time it is read.

    An attribute can be decorated with this class is the same way as with a normal `property`. It adds the possibility
    to invalidate the cache when necessary.
    """

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        # type: (Optional[Callable], Optional[Callable], Optional[Callable], Optional[str]) -> None
        """Initialize the `CachedProperty`.

        Parameters
        ----------
            fget, fset, fdel : function, optional
                Getter, setter, and deleter functions.

            doc : str, optional
                Docstring of the property.
        """
        super(CachedProperty, self).__init__(fget, fset, fdel, doc)
        self.__cache = None
        self.__dirty = True

    def __get__(self, instance, owner=None):
        # type: (Any, Optional[type]) -> Any
        """Get the value of the property.

        This method checks if the cache of this property is still valid first. If it is, it simply returns the cached
        value. If it isn't, it calls the `super()` to recompute the cached variable, stores it, and then returns the
        newly calculated value.

        Parameters
        ----------
            instance : any
                The instance through which the attribute is accessed.

            owner : type, optional
                The owner of the attribute.

        Returns
        -------
            any
                The value of the attribute.
        """
        if self.__dirty:
            self.__cache = super(CachedProperty, self).__get__(instance, owner)
            self.__dirty = False
        return self.__cache

    def invalidate(self):
        # type: () -> None
        """Marks the cache of the property as invalid, prompting its recomputation the next time it is accessed."""
        self.__dirty = True


def parse_string(s):
    # type: (str) -> Union[str, np.ndarray, float]
    """Convert a string to a numpy array of floats or float if possible.

    The string is returned unchanged if it cannot be converted to a numpy array of floats or float.

    Parameters
    ----------
        s : str
            String to be converted.

    Returns
    -------
        str or np.ndarray or float
            Parsed string or the string itself.
    """
    v = re.sub(r'[\[\]]', '', s)

    if ',' in v:
        v = v.split(',')
    elif ';' in v:
        v = v.split(';')

    try:
        v = np.atleast_1d(np.array(v, dtype=float))
        if v.size == 1:
            v = v[0]
        return v
    except ValueError:
        return s


def parse_cmdows_value(elem):
    # type: (etree._Element) -> Union[str, np.ndarray, float]
    """Convert an XML element from a CMDOWS file to a value.

    Parameters
    ----------
        elem : :obj:`_Element`
            `etree._Element` to convert.

    Returns
    -------
        str or np.ndarray or float
            Converted element.
    """
    if len(list(elem)) > 1:
        return np.array([parse_string(child.text) for child in elem])
    else:
        return parse_string(elem.text)


def normalized_to_bounds(driver):
    # type: (Type[Driver]) -> Type[NormalizedDriver]
    """Decorate a `Driver` to adjust its ``adder``/``scaler`` attributes normalizing the ``desvar``s.

    This decorator automatically adjusts the adder and scalar attributes of the design variables belonging to the
    targeted ``OpenMDAO`` `Driver` class such that the design variables are normalized to their bounds.

    Parameters
    ----------
        driver : :obj:`Driver`
            `Driver` to normalize the design variables of.

    Returns
    -------
        :obj:`NormalizedDriver`
            Instance of `NormalizedDriver` which inherits from the given `Driver`.

    Examples
    --------
        @normalized_to_bounds\n
        class MyNormalizedDriver(Driver):
            # My design variables will now automatically be normalized to their bounds.
            pass
    """

    class NormalizedDriver(driver):
        """Wrapper class for the `normalized_to_bounds` decorator.

        This class adds a static function to the `Driver` it inherits from, which will intercept all `add_desvar()`
        calls to the wrapped `Driver` class to change its ``adder``/``scaler`` attributes depending on the given
        upper and lower bounds.
        """

        @staticmethod
        def normalize_to_bounds(func):
            # type: (Callable) -> Callable
            """Wrap the function handle of the `add_desvar()` function.

            Parameters
            ----------
                func : function
                    Function handle of the `add_desvar()` function.

            Returns
            -------
                func : function
                    Function wrapping the `add_desvar()` function, which adds logic to calculate ``adder``/``scaler``.
            """

            def new_function(name,          # type: str
                             lower=None,    # type: Optional[Union[float, np.ndarray]]
                             upper=None,    # type: Optional[Union[float, np.ndarray]]
                             *args, **kwargs):
                # type: (...) -> None
                """Wrap the `add_desvar()` function call.

                Inner wrapper function which will set the ``adder`` and ``scaler`` `kwargs` of the wrapped
                `add_desvar()` method before calling it.

                Parameters
                ----------
                    name : str
                        Name of the design variable to add.

                    lower : float or list of float, optional
                        Lower bound(s) of the design variable.

                    upper : float or list of float, optional
                        Upper bound(s) of the design variable.

                    *args
                        Any extra, ordered arguments to pass to the `add_desvar()` method.

                    **kwargs
                        Any extra, named arguments to pass to the `add_desvar()` method.
                """
                if lower is not None:
                    adder = -lower
                else:
                    adder = 0.

                if upper is not None:
                    scaler = 1./(upper + adder)
                else:
                    scaler = 1.

                if len(args) > 4:
                    args = args[:-1]
                elif len(args) > 3:
                    args = args[:-1]

                if 'adder' in kwargs:
                    del kwargs['adder']
                if 'scaler' in kwargs:
                    del kwargs['scaler']

                func(name, lower, upper, adder=adder, scaler=scaler, *args, **kwargs)

            return new_function

        def __getattribute__(self, item):
            """Intercept any calls to the `add_desvar()` method of the Driver class.

            This ``hook`` checks if `add_desvar()` is called. If so, it returns the wrapped function instead of the
            clean `add_desvar()` call.

            Parameters
            ----------
                item : str
                    Name of the attribute.

            Returns
            -------
                any
                    The attribute that was requested or the wrapped call to `add_desvar()` if it is requested.
            """
            x = super(NormalizedDriver, self).__getattribute__(item)
            if item in ['add_desvar']:
                return self.normalize_to_bounds(x)
            else:
                return x

    return NormalizedDriver


re_sys_name_char = re.compile(r'[^_a-zA-Z0-9]')
re_sys_name_starts = re.compile(r'^[a-zA-Z]')


def str_to_valid_sys_name(string):
    # type: (str) -> str
    """Ensures a given string is a valid OpenMDAO system name."""
    sys_name = re_sys_name_char.sub('', string)
    while not re_sys_name_starts.match(sys_name):
        sys_name = sys_name[1:]
    return sys_name
