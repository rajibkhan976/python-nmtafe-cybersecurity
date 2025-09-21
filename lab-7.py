# Name: Rajib Hossain Khan
# Student ID: 20145454
# Version: 202009081123

import os
file = open("mbox.txt", "r")
print(type(file))

movie01 = "12 Monkeys"
movie02 = "The Godfather"
movie03 = "Police Academy"
movie04 = "Police Academy 2"
movie05 = "Police Academy 3"
movie06 = "Police Academy 4"
movie07 = "Police Academy 5"
movie08 = "Police Academy 6"
movie09 = "Police Academy 7"
movie10 = "Police Academy 8"
with open("movie-list.txt", "w") as f:
    f.write(movie01 + "\n")
    f.write(movie02 + "\n")
    f.write(movie03 + "\n")
    f.write(movie04 + "\n")
    f.write(movie05 + "\n")
    f.write(movie06 + "\n")
    f.write(movie07 + "\n")
    f.write(movie08 + "\n")
    f.write(movie09 + "\n")
    f.write(movie10 + "\n")
    f.close()

movie11 = "Police Academy 9"
movie12 = "Police Academy 10"
movie13 = "Police Academy 11"
movie14 = "Police Academy 12"
movie15 = "Police Academy 13"
with open("movie-list.txt", "w") as f:
    f.write(movie11 + "\n")
    f.write(movie12 + "\n")
    f.write(movie13 + "\n")
    f.write(movie14 + "\n")
    f.write(movie15 + "\n")
    f.close()

movie16 = "Police Academy 14"
movie17 = "Police Academy 15"
movie18 = "Police Academy 16"
movie19 = "Police Academy 17"
movie20 = "Police Academy 18"
with open("movie-list.txt", "a") as f:
    f.write(movie16 + "\n")
    f.write(movie17 + "\n")
    f.write(movie18 + "\n")
    f.write(movie19 + "\n")
    f.write(movie20 + "\n")
    f.close()

newFile = open("movie-list.txt", "r")
os.remove("C:/Users/rajib/OneDrive/Documents/tafe-python/movie-list.txt")

# get a correct file name from the user until the file is found
# get a letter and a string from the user once the file is found
# the leter should be a single letter
# read the file and get the no of occurences of the letter
# check if the string exists in the file
# print out the result
# write the result in a new file

# initiating the variables required to accomplish the task
fileName = None
file = None
letter = None
letterCount = 0

# promting for the filename until a file can be found
while not fileName or not file:
    fileName = input("Enter the name of the file: ")
    # trying to open the file name if the user provided value is not empty
    if fileName.strip():
        try:
            # opening the file
            file = open(fileName.strip())
        # handling file not found exception
        except FileNotFoundError:
            print(f"{fileName} does not exist. Please try again.")
    # asking for the letter & string user wants to search once the file is found
    if file != None:
        # promting user to enter a valid letter
        while not letter:
            searchLetter = input("Enter a letter to count: ")
            # checking the validity of user input
            if searchLetter.strip().isalpha() and len(searchLetter) == 1:
                letter = searchLetter.strip()
            else:
                print(
                    "Only a single letter of the alphabet is allowed. Please try again.")
        # resding the file
        data = file.read()
        # couting the occurrences of the letter
        letterCount = data.count(letter)
        # asking for the string user wants to search
        userString = input("Enter a string to search for: ")
        # printing the count of the letter
        result1 = f'There are {letterCount} occurrences of the letter "{letter}".'
        result2 = ""
        print(result1)
        # searching for the string and printing the result
        if data.find(userString) != -1:
            result2 = f'The string "{userString}" exists in the file.'
            print(result2)
        else:
            result2 = f'The string "{userString}" does not exist in the file.'
            print(result2)
        with open("result.txt", "a") as f:
            f.write(result1 + "\n")
            f.write(result2 + "\n")
