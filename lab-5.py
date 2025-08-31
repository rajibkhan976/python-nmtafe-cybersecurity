# import random

# a = random.randint(1, 100)
# b = random.randint(1, 100)

# result = a + b
# userInput = 0

# while result != userInput:
#     try:
#         if result == userInput:
#             break
#         userInput = input(f"Please enter the result of {a} + {b} = ")
#         userInput = int(userInput)
#     except:
#         print("Please enter a valid integer")


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
