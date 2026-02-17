s = 'kn176egw@1!3938!!!!@##jfdnhkguh???!?!?e738r'
# {'?': 5, '!': 7, '@':2, '#' : 2}

d = {'?': 0, '!': 0, '@': 0, '#': 0}

for i in s:
    if i in list(d.keys()):
        d[i] += 1

print(d)