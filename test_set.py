import pytest


def test_keyerror():
    s = {1, 2, 3, 5}
    try:
        s.remove(4)
        assert s == {1, 2, 3, 5}
    except KeyError:
        pass


def test_add():
    s = set()
    s.add(3)
    assert s == {3}


@pytest.mark.parametrize(
    "to_update,update",
    [({2, 3, 4}, {1, 2, 3, 4}),
     ({}, {1}),
     ("123", {1, "1", "2", "3"}),
     ([1, 2, 3], {1, 2, 3}),
     pytest.param(True, {1, True}, marks=pytest.mark.xfail)]

)
def test_update(to_update, update):
    s = {1}
    s.update(to_update)
    assert s == update
