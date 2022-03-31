"""Test unit for the analysis code"""

from analysis import analyser
import numpy as np

def test_not_array_predict():
    '''Test when predict is not an array'''

    passed = False

    try:

        error = analyser("string",[[0,1],[0,1]])

    except TypeError:

        passed = True

    assert passed

def test_not_array_real():
    '''Test when real is not an array'''

    passed = False

    try:

        error = analyser([[0,1],[0,1]],"string")

    except TypeError:

        passed = True

    assert passed


def test_different_shapes():
    '''Test when predict and real don't have the same shape'''

    passed = False

    try:

        error = analyser(np.array([0,1,2]),np.array([0,1,2,3]))

    except IndexError:

        passed = True

    assert passed

def test_error_0():
    '''Test error=0'''

    expect = 0
    error = analyser(np.array([0,1,2]),np.array([0,1,2]))
    assert np.isclose(error,expect)

def test_error_1():
    '''Test error=1'''

    expect = 1
    error = analyser(np.array([1,0]),np.array([0,1]))
    assert np.isclose(error,expect)

def test_error_quarter():
    '''Test error=1/4'''

    expect = 0.25
    error = analyser(np.array([0,1,0,0]),np.array([0,0,0,0]))
    assert np.isclose(error,expect)

