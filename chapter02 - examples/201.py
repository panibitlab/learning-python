'''
this code finds odd and even values in the given list.
'''

a = [1, 2, 3, 4, 5, 10, 7, 9, 8]  # given list.

odd = []
even = []

for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("odd numbers: ", odd)
print("even numbers: ", even)
