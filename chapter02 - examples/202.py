'''
this code checks if a given string contains specific characters.
'''

# the code can be written as follows:

str = "abrt123?@#!54o?!"
signs = ['!', '?', '#', '@']
contained_signes = []

a = list(str)

for i in a:
    if i in signs:
        contained_signes.append(i)

print(contained_signes)


# or it can be written like so:
str = "abrt123?@#!54o?!"

result = []

for ch in str:
    if ch == '!' or ch == '?' or ch == '#' or ch == '@' :
        result.append(ch)

print(result)
