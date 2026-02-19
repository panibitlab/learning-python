def dict_avg(d: dict) -> dict:
    """returns avg of each list given in a dictionary as values."""
    if not isinstance(d, dict):
        raise TypeError("Input must be a dictionary.")

    result = {}

    for key, values in d.items():

        if not isinstance(values, list):
            raise TypeError(f"Value of '{key}' must be a list.")

        if len(values) == 0:
            raise ValueError(f"List for '{key}' cannot be empty.")

        if not all(isinstance(x, (int, float)) for x in values):
            raise TypeError(f"All elements in list '{key}' must be numbers.")

        avg = sum(values) / len(values)
        result[f"{key}_avg"] = int(avg)

    return result


print(dict_avg({'l1': [1, 2, 3, 5], 'l2': [2, 3, 6, 1], 'l3': [3, 7, 8, 9]}))
