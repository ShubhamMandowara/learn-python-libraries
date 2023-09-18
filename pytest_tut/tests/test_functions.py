from src.functions import increase_value
import pytest

def test_increment_value_function_simple():
    value = 10
    assert value + 5 == increase_value(value=value)
    assert value != increase_value(value)


@pytest.mark.dev
def test_increment_value_function_group():
    value = 10
    assert value + 5 == increase_value(value=value)
    assert value != increase_value(value)


@pytest.fixture
def values():
    return 10

@pytest.mark.dev
def test_increment_value_function_fixture(values):
    assert values + 5 == increase_value(value=values)
    assert values != increase_value(values)

@pytest.mark.parametrize("value",[10, 20, 30, 40, 50])
def test_increment_value_function_parameter(value):
    assert value + 5 == increase_value(value=value)
    assert value != increase_value(value)

@pytest.mark.skip
def test_increment_value_function_skip(value):
    assert value + 5 == increase_value(value=value)
    assert value == increase_value(value)


@pytest.mark.xfail
def test_increment_value_function_fail(value):
    assert value + 5 == increase_value(value=value)
    assert value == increase_value(value)