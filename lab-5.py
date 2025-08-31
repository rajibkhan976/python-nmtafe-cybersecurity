# # Name: Rajib Hossain Khan
# # Student ID: 20145454
# # Version: 202009081123

# x = 0
# while True:
#     print(x)
#     x += 1

import random

a = random.randint(1, 100)
b = random.randint(1, 100)

result = a + b
userInput = 0

while result != userInput:
    try:
        if result == userInput:
            break
        userInput = input(f"Please enter the result of {a} + {b} = ")
        userInput = int(userInput)
    except:
        print("Please enter a valid integer")
