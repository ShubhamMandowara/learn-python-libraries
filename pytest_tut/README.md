### Pytest
Make it easy to test your functionality. From simple, readable tests to complex functionality tests for your application and libraries.
Rmoves the error from coming into production


Example: Your function take integers value and return a integer.

Without test: There will be problem in behaviour of the function. what it will return

With test: On small code or functions you are confident about the result.

Test helps to make more complex code reliable and easy to add new functionality on top of existing functionality.

    def full_name_with_hello(first_name:str, last_name:str):
        return 'Hello' + first_name + ' ' + last_name

    def test_full_name_with_hello():
        first_name = 'Mando'
        last_name = 'ai'
        assert 'Hello' + first_name + ' ' + last_name == full_name_with_hello(first_name, last_name)


- All the file folder names that start or ends with 'test' will run  on pytest command
`pytest . `
- If want to run specific tests file    `pytest filename.py`
- we can group the tests with tests `@pytest.mark.groupname` and we test those specific tests based on group name using `pytest -m group_name -v`

### Fixture
Are those functions which will run before the test case to which it applied.
- Can feed data from database, url to test
- we can attach fixture function to the tests and it will run and return the data to the test before executing each test

To mark a function as fixture
use `@pytest.fixture`

    @pytest.fixture
    def values():
        return 10

    def test_increase(values):
        assert 15 == increase_value(input_value)


Can make fixture functions in the file to make them accessible accross all tests

#### file.py

    import pytest
        @pytest.fixture
    def value():
        return 10

### in other tests
    import pytest

    def test_increase(values):
        assert 15 == increase_value(input_value)


## parameterize tests
we can give parameters to run tests on many inputs

    import pytest
    @ptytest.mark.parameterize("input", [10,20,30,40])
    def test_increase(input):
        assert input + 5 == increment_value(input)

## to skip the test
We can use skip anotation
@pytest.mask.skip

## to fail funciton
we can use pytest.mark.xfail


# To run tests in parallel
use

    pytest -n 3

To run 3 parallel test at a time
