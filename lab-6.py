# Name: Rajib Hossain Khan
# Student ID: 20145454
# Version: 202009081123

# declaring counter to control the loop
count = 1
# declaring list to add the valid words
wordList = []
# declaring list to track the count of letters in the valid word
countList = []

# declaring a loop to get input from the user
while count < 6:  # checking to counter to determine when to break the loop
    newWord = input(f"Enter word {count} of 5: ")  # getting user input
    validWord = newWord.strip()  # stripping of the spaces
    # validating the user input
    if validWord.find("-") == -1 and validWord.isspace() == False:
        wordList.append(validWord)  # appending valid word to the list
        # appending valid word'd length to the list
        countList.append(len(validWord))
        count += 1  # incrementing the counter

maxCount = max(countList)  # determing max count
# determing the word with max count
result = wordList[countList.index(maxCount)]
print(f"{result} has the most letters {maxCount}")  # printing the result


# declare a counter
# declare a list to store valid words
# declare a list to keep track of the lengths of the valid words
# get user input for 5 words
# remove all space from start & end of user input
# validate the user input so that it does npt contain any hyphen or space
# add the word into the word list
# add the word lenght in the count list
# detemine the max count from the count list
# get the word with max lenght by using the index of the max count from count list
