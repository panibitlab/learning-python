'''
this code receives a string and counts its number of uppercase and lowercase characters.
'''

upper_counter = 0
lower_counter = 0
non_letter_counter = 0

s = input("input string: ")

for i in s:
    if i.isupper():
        upper_counter += 1
    elif i.islower():
        lower_counter += 1
    else:
        non_letter_counter += 1

print(f"number of uppercase letters: {upper_counter}")
print(f"number of lowercase letters: {lower_counter}")
print(f"number of non letters: {non_letter_counter}")

