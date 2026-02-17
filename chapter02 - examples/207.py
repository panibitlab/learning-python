d = {'g1': [1,100,5,98,72,101], 'g2': [5,71,49,63]}
# result = {'g1': 101, 'g2': 71}

for i in d:
    d[i] = max(d[i])

print(d)

#or

result = {}

for k, v in d.items():
    result.setdefault(k, max(v))

print(result)
