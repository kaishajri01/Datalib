import pytest
import numpy as np
from src.statistics import (calculate_mean, calculate_median, calculate_mode, 
                                 calculate_std, correlation, t_test, chi_square_test)

def test_calculate_mean():
    data = [1, 2, 3, 4, 5]
    assert calculate_mean(data) == 3

def test_calculate_median():
    data = [1, 2, 3, 4, 5]
    assert calculate_median(data) == 3

def test_calculate_mode():
    data = [1, 2, 2, 3, 4]
    assert calculate_mode(data) == 2

def test_calculate_std():
    data = [1, 2, 3, 4, 5]
    assert np.isclose(calculate_std(data), 1.414, atol=0.001)

def test_correlation():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    assert correlation(x, y) == 1

def test_t_test():
    data1 = [1, 2, 3, 4, 5]
    data2 = [5, 6, 7, 8, 9]
    stat, pval = t_test(data1, data2)
    assert pval > 0.05

def test_chi_square_test():
    observed = [10, 20, 30]
    expected = [10, 20, 30]
    stat, pval = chi_square_test(observed, expected)
    assert pval > 0.05
