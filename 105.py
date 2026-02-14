'''
this code prints half diamond using *s.
'''
n = int(input())

#printing the upper part with the main line.
for i in range(1, n + 1):
    print(i * "*")

#printing the lowerpart.
for i in range(n - 1, 0, -1):
    print(i * "*")