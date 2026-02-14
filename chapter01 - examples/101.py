#lets begin!
'''
this code receives a string and prints its number of digits.
'''

counter = 0

num = int(input("input number: "))

while num != 0:
    num = num // 10
    counter += 1

print(counter)