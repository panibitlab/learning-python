'''
this code will calculate max avg of 5 interaction of random made numbers.
'''
import random

max_avg = 0

for i in range(5):
    first_num = random.randint(0,100)
    second_num = random.randint(0,100)
    interaction_avg = (first_num + second_num) / 2

    if interaction_avg > max_avg:
        max_avg = interaction_avg

    print(f"interaction {i}: first_num: {first_num}, second_num: {second_num}")

print("max average is: ", max_avg)