d = {'a': 10, 'b': 12, 'c': 13, 'd': 18, 'e': 22}
# [12, 18]
l_3 = []

for k, v in d.items():
    if v % 3 == 0:
        l_3.append(v)

print(l_3)
