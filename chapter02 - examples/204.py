list = ['a', 1, 2, 5, 10, 'hello', 'b', 7, 10.2]
# {"str" : 3, "int" : 5}

str_counter = 0
int_counter = 0
d = {}

for i in list:
    if isinstance(i, str):
        str_counter += 1
    elif isinstance(i, int):
        int_counter += 1

d['str'] = str_counter
d['int'] = int_counter

print(d)

# or

result = {'str': 0, 'int': 0}

for i in list:
    if isinstance(i, str):
        result['str'] += 1
    elif isinstance(i, int):
        result['int'] += 1

print(result)