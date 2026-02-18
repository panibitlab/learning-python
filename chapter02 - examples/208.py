num_list = [1, 2, 3, 13, 12, 16]
# [256, 144, 4]

squ = []

num = list(set(num_list))
for i in num:
    if i % 2 == 0:
        squ.append(i ** 2)

print(squ)
