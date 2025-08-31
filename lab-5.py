# # Name: Rajib Hossain Khan
# # Student ID: 20145454
# # Version: 202009081123

# section 2 question 6
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

# section 3 question 4

oneWord = input("Please enter one word: ")
anotherWord = input("Please enter another word: ")
matchingLetter = input("Please enter a letter you want to match: ")
countOfLetterInFirstWord = 0
countOfLetterInSecondWord = 0

for i in oneWord:
    if matchingLetter == i:
        countOfLetterInFirstWord += 1

for c in anotherWord:
    if matchingLetter == c:
        countOfLetterInSecondWord += 1

if countOfLetterInFirstWord > countOfLetterInSecondWord:
    print(f"{matchingLetter} has more mtaches in {oneWord}")
elif countOfLetterInSecondWord > countOfLetterInFirstWord:
    print(f"{matchingLetter} has more mtaches in {anotherWord}")
else:
    print(f"{matchingLetter} has same number of matches in {oneWord} & {anotherWord}")

# section 4

numCount = 0
total = 0
userNum = input(f"Enter 'done' or number {numCount}: ")

# running a loop to check if user wants to finish the task
while userNum != "done":
    # checking if the user input is a number
    if userNum.isnumeric():
        try:
            userNum = int(userNum)
            total += userNum
            numCount += 1
        except ValueError:
            print(ValueError)
        userNum = input(f"Enter 'done' or number {numCount}: ")
    else:
        print("Your input was invalid, try again")
        userNum = input(f"Enter 'done' or number {numCount}: ")

# printing the output of the task
print(f"You input a total of {numCount} numbers.")
print(f"The sum of those numbers is {total}")
