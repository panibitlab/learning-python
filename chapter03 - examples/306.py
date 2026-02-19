def max_of_two(a: int or float, b: int or float) -> int or float:
    """returns max of two int/float inputs."""
    if not isinstance(a, int or float) or not isinstance(b, int or float):
        raise Exception("inputs must be either int or float.")

    max_2 = max(a, b)

    return max_2


def max_of_three(a: int or float, b: int or float, c: int or float) -> int or float:
    """by using max_of_two, returns max of three int/float inputs."""
    if not isinstance(a, int or float) or not isinstance(b, int or float) or not isinstance(c, int or float):
        raise Exception("inputs must be either int or float.")

    max_3 = max(max_of_two(a, b), c)

    return max_3


print(max_of_three(3, 5, 8))
