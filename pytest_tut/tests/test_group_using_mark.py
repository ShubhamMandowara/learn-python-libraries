from src import functions
import pytest

@pytest.mark.first_version
def test_functions():
    assert 15 == functions.increase_value(value=10)