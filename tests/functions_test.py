import numpy as np

import vaex


def test_numpy_function_isnan():
    x = np.array([-1, 2, 3, 4, np.nan, np.nan, np.nan, -2, -3, 5, 10])
    ds = vaex.from_arrays(x=x)
    assert ds.selected_length('isnan(x)') == 3
    assert ds.selected_length('~(isnan(x))') == 8
    assert ds[(ds.x > 3) | (np.isnan(ds.x))].x.tolist() == [4., np.nan, np.nan, np.nan,  5., 10.]


def test_numpy_function_isinf():
    x = np.array([-1, 2, 3, 4, np.inf, np.inf, np.inf, -2, -3, 5, 10])
    ds = vaex.from_arrays(x=x)
    assert ds.selected_length('isinf(x)') == 3
    assert ds.selected_length('~(isinf(x))') == 8
    assert ds[(ds.x > 3) | (np.isinf(ds.x))].x.tolist() == [4., np.inf, np.inf, np.inf,  5., 10.]
