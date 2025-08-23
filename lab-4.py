# # Name: Rajib Hossain Khan
# # Student ID: 20145454
# # Version: 202009081123

import random


def guessTheNumber(startNumber, endNumber, guess):
    theAnswer = random.randint(startNumber, endNumber)
    print(f"The answer is {theAnswer}")
    if theAnswer == guess:
        return True
    else:
        return False


lowNumber = int(input("Enter the lowest number: "))
highNumber = int(input("Enter the highest number: "))
userGuess = int(
    input(f"Enter your guess between {lowNumber} - {highNumber}: "))

if guessTheNumber(lowNumber, highNumber, userGuess):
    print("You guesses it!")
else:
    print("Oops, wrong")


def printTheLine(number):
    print("the dumber the reason the more it must be done\n"*number)


printTheLine(4)


def greetings():
    print("Welcome to Arrestaurant. May I take your statement?")


greetings()


def compareWith10(number):
    if number > 10:
        print("The number is greater than 10")
    elif number < 10:
        print("The number is less than 10")
    else:
        print("The number is equal to 10")


compareWith10(9)


def diceGame():
    return random.randint(1, 6)


print(diceGame())
