# [1,2,5,4,3]
# {'even' : [2,4], 'odd' : [1,5,3]}
def odd_even(l: list) -> dict:
    """returns even & odd values in a dictionary, given as a list."""
    if not isinstance(l, list):
        raise TypeError("input must be a list.")

    d = {'even': [], 'odd': []}
    for i in l:
        if i % 2 == 0:
            d['even'].append(i)
        else:
            d['odd'].append(i)
    return d


print(odd_even([1, 2, 5, 4, 3]))
