def intersection_union(d:dict) -> dict:
    """returns intersection & union of list inputs, given as dict values. """
    result = {'intersection' : d[list(d.keys())[0]], 'union' : d[list(d.keys())[0]]}

    for k, v in d.items():
        result['intersection'] = result['intersection'].intersection(v)
        result['union'] = result['union'].union(v)

    return result


print(intersection_union({'s1': {1,2,3,4}, 's2': {1,5,7,3}, 's3': {2,1,8,9}}))