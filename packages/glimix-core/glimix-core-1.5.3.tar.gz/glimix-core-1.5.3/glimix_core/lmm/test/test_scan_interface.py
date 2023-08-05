from numpy import array, inf, nan, ones

import pytest
from glimix_core.lmm import FastScanner
from numpy_sugar.linalg import economic_qs


def test_scan_interface():
    y = array([-1.0449132, 1.15229426, 0.79595129])
    low_rank_K = array([[5., 14., 23.], [14., 50., 86.], [23., 86., 149.]])
    QS = economic_qs(low_rank_K)
    X = ones((3, 1))

    y[0] = nan
    with pytest.raises(ValueError):
        FastScanner(y, X, QS, 0.5)

    y[0] = inf
    with pytest.raises(ValueError):
        FastScanner(y, X, QS, 0.5)

    y[0] = 1
    X[0, 0] = nan
    with pytest.raises(ValueError):
        FastScanner(y, X, QS, 0.5)

    y[0] = 1
    X[0, 0] = 1
    with pytest.raises(ValueError):
        FastScanner(y, X, QS, -1)

    with pytest.raises(ValueError):
        FastScanner(y, X, QS, nan)
