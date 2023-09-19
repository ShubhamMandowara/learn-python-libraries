"""
This is for testing and checking pylint lib
"""


def function(first_arg: int, second_arg: int) -> int:
    """Function is to add two arguments
    Args:
        first_arg (int) : the first argument
        second_arg (int) : the second argument
    Returns:
        int: sum of the two arguments
    """
    return first_arg + second_arg


if __name__ == "__main__":
    print(function(first_arg=10, second_arg=12))
