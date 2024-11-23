import pytest
from solution import sum_two_ints, sum_two_strs, sum_two_floats, sum_two_bools


def test_ints():
    assert sum_two_ints(1, 2) == 3
    with pytest.raises(TypeError, match="Argument 'b' must be of type int, got str"):
        sum_two_ints(1, "2")
    with pytest.raises(TypeError, match="Argument 'b' must be of type int, got bool"):
        sum_two_ints(1, True)
    with pytest.raises(TypeError, match="Argument 'b' must be of type int, got float"):
        sum_two_ints(1, 1.1)


def test_strs():
    assert sum_two_strs("abo", "ba") == "aboba"
    with pytest.raises(TypeError, match="Argument 'b' must be of type str, got int"):
        sum_two_strs('1', 2)
    with pytest.raises(TypeError, match="Argument 'b' must be of type str, got bool"):
        sum_two_strs('1', True)
    with pytest.raises(TypeError, match="Argument 'b' must be of type str, got float"):
        sum_two_strs('1', 1.1)


def test_floats():
    assert sum_two_floats(1.0, 2.0) == 3.0
    with pytest.raises(TypeError, match="Argument 'b' must be of type float, got str"):
        sum_two_floats(1.1, "2.2")
    with pytest.raises(TypeError, match="Argument 'b' must be of type float, got bool"):
        sum_two_floats(1.1, True)
    with pytest.raises(TypeError, match="Argument 'b' must be of type float, got int"):
        sum_two_floats(1.1, 1)


def test_bools():
    assert sum_two_bools(True, False)
    with pytest.raises(TypeError, match="Argument 'b' must be of type bool, got int"):
        sum_two_bools(True, 2)
    with pytest.raises(TypeError, match="Argument 'b' must be of type bool, got str"):
        sum_two_bools(True, "2")
    with pytest.raises(TypeError, match="Argument 'b' must be of type bool, got float"):
        sum_two_bools(True, 2.2)
