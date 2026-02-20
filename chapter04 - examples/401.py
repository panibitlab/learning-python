def factorial(n):
    # n! = n * (n-1)!
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
