import pytest
from calc import Calc


@pytest.mark.usefixtures('test_fixture')
def test_sum_001():
    assert Calc.sum(1, 1) == 2


# @pytest.mark.usefixtures('test_fixture')
@pytest.mark.skip()
def test_sum_002(test_fixture, test_fixture_1):
    print(test_fixture)
    assert Calc.sum(1, 5) == 8


TEST_CONST = True


@pytest.mark.skipif(TEST_CONST is True, reason="test skipif")
def test_sum_003(test_fixture, test_fixture_1):
    print(test_fixture)
    assert Calc.sum(1, 5) == 8


@pytest.mark.parametrize(
    ("a", "b", "c"), [
        (1, 1, 2),
        (1, -1, 0),
        (-1, 1, 0),
        (5, 7, 12),
        (0, 0, 0)
    ]
)
def test_sum_004(a, b, c):
    assert Calc.sum(a, b) == c

