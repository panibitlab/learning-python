#prime?

def prime_num(n : int) -> bool:
    """returns bool answer to the question: 'is the input given as an int, a prime num or not?' """
    if not isinstance(n, int):
        raise TypeError("input must be an int.")

    if n < 2:
        return False

    for i in range(2, int((n ** 0.5) + 1)):
        if n % i == 0:
            return False
    return True


print(prime_num(2))