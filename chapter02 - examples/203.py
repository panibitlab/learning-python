'''
this code checks the contents of a basket: counts the green and rotted ones. it stops once reaching a red apple.
'''

basket = ['green', 'rotted', 'green', 'red', 'rotted', 'green', 'red']

rotted_counter = 0
green_counter = 0

while True:
    apple = basket.pop(0)
    if apple == 'red':
        break
    elif apple == 'rotted':
        rotted_counter += 1
    else:
        green_counter += 1

print(f"number od green apples: {green_counter}")
print(f"number od rotted apples: {rotted_counter}")

