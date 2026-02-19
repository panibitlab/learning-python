def max_min_list(l: list) -> dict:
    """returns max, min and length of a given list, in dict form."""
    max_l = 0
    min_l = 0

    for i in l:
        if not isinstance(i, int or float):
            raise Exception("input must be a list of numbers.")
        else:
            max_l = max(l)
            min_l = min(l)

    d = {'max': max_l, 'min': min_l, 'length': len(l)}
    return d


print(max_min_list([1, 2, 3, 6, 2, 43]))


# or

def max_min_of_list(l: list) -> dict:
    return {'max': max(l), 'min': min(l), 'length': len(l)}


print(max_min_of_list([1, 2, 3, 6, 2, 43]))
