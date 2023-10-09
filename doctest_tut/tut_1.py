def hello_with_name(name: str) -> str:
    """This function is for saying hello to a person

    >>> hello_with_name("Mando AI")
    'Hello Mando AI'

    >>> sum_value(1,2)
    3

    Args:
        name (str): Name of the person

    Returns:
        str: Hello with name
    """
    return "Hello " + name


def sum_value(num_1: int, num_2: int) -> int:
    """Sum  two values

    >>> sum_value(1,2)
    3


    Args:
        num_1 (int): Number 1
        num_2 (int): Number 2

    Returns:
        int: sum of two values
    """
    return num_1 + num_2


if __name__ == "__main__":
    print(hello_with_name("Mando AI"))
