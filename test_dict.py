import pytest


def test_keyerror():
    d = {'alice': 10}
    try:
        assert d['alic'] == 10
    except KeyError:
        pass


def test_pop():
    d = {'alice': 10, 'bob': 20}
    d.pop('bob')
    assert d == {'alice': 10}


@pytest.mark.parametrize(
    "to_update,update",
    [({2: 2}, {1: 1, 2: 2}),
     ({1: 5, 1: 5, 3: 3}, {1: 5, 3: 3}),
     pytest.param(
         {1: 'yes', 1.0: 'no', True: 'maybe'},
         {1: 'yes', 1.0: 'no', True: 'maybe'}, marks=pytest.mark.xfail)],
)
def test_update(to_update, update):
    d = {1: 1}
    d.update(to_update)
    assert d == update
