from src import functions
import pytest

@pytest.mark.first_version
def test_functions():
    assert 15 == functions.increate_value(value=10)