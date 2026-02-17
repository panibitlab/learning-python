list = [1,2,1,5,6,1,1,5,'a','a','b',5]
d = {}

for i in list:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)

#or

result = {}

for i in list:
    result.setdefault(i, 0)
    result[i] += 1

print(result)


