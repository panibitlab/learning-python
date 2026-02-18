l = [1, 12.5, 'a', 'salam', 190]
# ['a', 'salam']
str_l = []

for i in l:
    if isinstance(i, str):
        str_l.append(i)

print(str_l)

