"""Functions for validating function arguments."""

import numbers

import numpy as np
import pandas as pd


def _check_type(obj, base, allow_none):
    """Check whether an object is an instance of a base type.

    Parameters
    ----------
    obj : object
        The object to be validated.
    base : type
        The base type that `obj` should be an instance of.
    allow_none : bool
        Indicates whether the value None should be allowed to pass through.

    Returns
    -------
    obj : base type or None
        The validated object.

    Raises
    ------
    TypeError
        If `obj` is not an instance of `base`.
    """
    # Validate `base`
    if allow_none and obj is None:
        return None
    elif isinstance(obj, base):
        return obj
    else:
        expect = base.__name__
        actual = type(obj).__name__
        raise TypeError(f"Invalid type. Expected: {expect}. Actual: {actual}.")


def check_bool(tf, *, allow_none=False):
    """Validate boolean function arguments.

    Parameters
    ----------
    tf : object
        The object to be validated.
    allow_none : bool, optional (default: False)
        Indicates whether the value None should be allowed.

    Returns
    -------
    tf : bool or None
        The validated bool.

    Raises
    ------
    TypeError
        If `tf` is not an instance of bool.
    """
    return _check_type(tf, bool, allow_none)


def check_int(num, *, minimum=None, maximum=None, allow_none=False):
    """Validate integer function arguments.

    Parameters
    ----------
    num : object
        The object to be validated.
    minimum : int, optional (default: None)
        The minimum value that `num` can take (inclusive).
    maximum : int, optional (default: None)
        The maximum value that `num` can take (inclusive).
    allow_none : bool, optional (default: False)
        Indicates whether the value None should be allowed.

    Returns
    -------
    num : integer type or None
        The validated integer.

    Raises
    ------
    TypeError
        If `num` is not an integer.
    ValueError
        If any of the optional minimum and maximum value constraints are
        violated.
    """
    num = _check_type(num, numbers.Integral, allow_none)

    if minimum is not None:
        minimum = check_int(minimum)
        if num < minimum:
            raise ValueError(f"Parameter must be at least {minimum}.")

    if maximum is not None:
        maximum = check_int(maximum)
        if num > maximum:
            raise ValueError(f"Parameter must be at most {maximum}.")

    return num


def check_float(num, *, positive=False, minimum=None, maximum=None,
                allow_none=False):
    """Validate floating-point number function arguments.

    Parameters
    ----------
    num : object
        The object to be validated.
    positive : bool (default: False)
        If True, `num` must be positive. If False, `num` can be any float.
    minimum : float, optional (default: None)
        The minimum value that `num` can take (inclusive).
    maximum : float, optional (default: None)
        The maximum value that `num` can take (inclusive).
    allow_none : bool, optional (default: False)
        Indicates whether the value None should be allowed.

    Returns
    -------
    num : float type or None
        The validated float.

    Raises
    ------
    TypeError
        If `num` is not a float.
    ValueError
        If any of the optional positivity or minimum and maximum value
        constraints are violated.
    """
    num = _check_type(num, numbers.Real, allow_none)

    positive = check_bool(positive)
    if positive and num <= 0.0:
        raise ValueError(f"Parameter must be positive.")

    if minimum is not None:
        minimum = check_float(minimum)
        if num < minimum:
            raise ValueError(f"Parameter must be at least {minimum}.")

    if maximum is not None:
        maximum = check_float(maximum)
        if num > maximum:
            raise ValueError(f"Parameter must be at most {maximum}.")

    return num


def check_data_1d(data, *, n_exact=None, n_min=None, n_max=None, copy=False,
                  dtype=None, order=None):
    """Preprocess and validate a one-dimensional array.

    Parameters
    ----------
    data : array-like
        The data array. If `data` is a scalar, it is interpreted as an array of
        shape (1,).
    n_exact : int, optional (default: None)
        Exact number of entries expected.
    n_min : int, optional (default: None)
        Minimum number of entries expected.
    n_max : int, optional (default: None)
        Maximum number of entries expected.
    copy : bool, optional (default: False)
        If True, the array will be copied. If False, the array might be copied
        depending on the behavior of numpy.array().
    dtype : str or type, optional (default: None)
        The desired data type for the feature matrix.
    order : str, optional (default: None)
        The desired memory layout of the array. See the numpy.array()
        documentation for details.

    Returns
    -------
    data : one-dimensional numpy.ndarray
        The validated one-dimensional array.

    Raises
    ------
    ValueError
        If the input array is empty or has more than one dimension, or if any of
        the optional constraints on the number of entries is violated.
    """
    # Coerce into a NumPy array
    data = np.array(data, dtype=dtype, copy=copy, order=order)

    # Coerce scalars to arrays
    if data.ndim < 1:
        data = data.reshape(-1)

    # Ensure array is at most one dimensional and non-empty
    if data.ndim > 1:
        raise ValueError(f"Array must be at most one-dimensional.")
    elif data.size == 0:
        raise ValueError(f"Array cannot be empty.")

    # Ensure every constraint on the number of entries is met
    n = data.shape[0]
    n_exact = check_int(n_exact, allow_none=True)
    n_min = check_int(n_min, allow_none=True)
    n_max = check_int(n_max, allow_none=True)
    if n_exact is not None and n_exact != n:
        raise ValueError(f"Expected {n_exact} entries, found {n}.")
    if n_min is not None and n_min > n:
        raise ValueError(f"Expected at least {n_min} entries, found {n}.")
    if n_max is not None and n_max < n:
        raise ValueError(f"Expected at most {n_max} entries, found {n}.")

    return data


def check_data_2d(data, *, n_exact=None, n_min=None, n_max=None, p_exact=None,
                  p_min=None, p_max=None, copy=False, dtype=None, order=None):
    """Preprocess and validate a two-dimensional array (i.e., a matrix).

    A matrix of shape (n, p) represents n observations of p features. That is,
    each of the n rows represents the p features of a single observation, and
    likewise each of the p columns represents all n observations of a single
    feature.

    If `data` is a scalar, it is interpreted as one observation of one feature
    and is coerced into a NumPy array of shape (1, 1).

    If `data` is an array of shape (n, ), then it is interpreted as n
    observations of a single feature and is coerced into a NumPy array of shape
    (n, 1). This means that if you want one observation of p features, then you
    must pass in a two-dimensional array of shape (1, p).

    If `data` is a pandas.DataFrame, the returned value will also be a
    pandas.DataFrame. Otherwise, the returned value is a numpy.ndarray.

    Parameters
    ----------
    data : array-like
        Matrix of shape (n, p) (n=number of observations, p=number of features).
    n_exact : int, optional (default: None)
        Exact number of observations (rows) expected.
    n_min : int, optional (default: None)
        Minimum number of observations (rows) expected.
    n_max : int, optional (default: None)
        Maximum number of observations (rows) expected.
    p_exact : int, optional (default: None)
        Exact number of features (columns) expected.
    p_min : int, optional (default: None)
        Minimum number of features (columns) expected.
    p_max : int, optional (default: None)
        Maximum number of features (columns) expected.
    copy : bool, optional (default: False)
        If True, the array will be copied. If False, the array might be copied
        depending on the behavior of numpy.array().
    dtype : str or type, optional (default: None)
        The desired data type for the feature matrix.
    order : str, optional (default: None)
        The desired memory layout of the array. See the numpy.array()
        documentation for details.

    Returns
    -------
    data : two-dimensional numpy.ndarray or pandas.DataFrame
        The validated two-dimensional array.

    Raises
    ------
    ValueError
        If the input array is empty or is has more than two dimensions, or if
        any of the optional constraints on the number of rows and columns is
        violated.
    """
    if isinstance(data, pd.DataFrame):
        # Potentially copy the DataFrame
        data = pd.DataFrame(data, index=data.index, columns=data.columns,
                            dtype=dtype, copy=copy)
    else:
        # Coerce into a NumPy array
        data = np.array(data, dtype=dtype, copy=copy, order=order)

        # Coerce scalars and 1D arrays to 2D arrays
        if data.ndim < 2:
            data = data.reshape((-1, 1), order=order)

    # Ensure at most two-dimensions and non-emptiness
    if data.ndim > 2:
        raise ValueError(f"Array must be at most two-dimensional.")
    elif data.size == 0:
        raise ValueError(f"Array cannot be empty.")

    # Ensure every constraint on the number of rows and columns is met
    # n = number of observations (rows), p = number of features (columns)
    n, p = data.shape
    n_exact = check_int(n_exact, allow_none=True)
    n_min = check_int(n_min, allow_none=True)
    n_max = check_int(n_max, allow_none=True)
    p_exact = check_int(p_exact, allow_none=True)
    p_min = check_int(p_min, allow_none=True)
    p_max = check_int(p_max, allow_none=True)
    if n_exact is not None and n_exact != n:
        raise ValueError(f"Expected {n_exact} rows, found {n}.")
    if n_min is not None and n_min > n:
        raise ValueError(f"Expected at least {n_min} rows, found {n}.")
    if n_max is not None and n_max < n:
        raise ValueError(f"Expected at most {n_max} rows, found {n}.")
    if p_exact is not None and p_exact != p:
        raise ValueError(f"Expected {p_exact} columns, found {p}.")
    if p_min is not None and p_min > p:
        raise ValueError(f"Expected at least {p_min} columns, found {p}.")
    if p_max is not None and p_max < p:
        raise ValueError(f"Expected at most {p_max} columns, found {p}.")

    return data


def check_random_state(random_state):
    """Validate random number generators and seeds.

    Parameters
    ----------
    random_state : numpy.random.RandomState, int, array-like, or None
        Either a numpy.random.RandomState instance or a valid seed for a
        numpy.random.RandomState object.

    Returns
    -------
    random_state : numpy.random.RandomState
        A ready-to-use random number generator.
    """
    if isinstance(random_state, np.random.RandomState):
        return random_state
    else:
        return np.random.RandomState(random_state)
