def average(*args):
    for i in args:
        if not isinstance(i, (int, float)):
            return Exception("parameters must be int or float.")
    return sum(args) / len(args)


print(average(3, 4, 5, 8))
