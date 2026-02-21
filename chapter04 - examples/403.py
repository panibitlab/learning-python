def average_kw(**kwargs):
    for i in kwargs:
        if not isinstance(kwargs[i], (int, float)):
            return Exception("parameters must be int or float.")
    return sum(kwargs.values()) / len(kwargs.keys())


print(average_kw(x=100, y=200, z=500))
