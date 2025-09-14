# Name: Rajib Hossain Khan
# Student ID: 20145454
# Version: 202009081123

# file = open("mbox.txt", "r")
# print(type(file))

# movie01 = "12 Monkeys"
# movie02 = "The Godfather"
# movie03 = "Police Academy"
# movie04 = "Police Academy 2"
# movie05 = "Police Academy 3"
# movie06 = "Police Academy 4"
# movie07 = "Police Academy 5"
# movie08 = "Police Academy 6"
# movie09 = "Police Academy 7"
# movie10 = "Police Academy 8"
# with open("movie-list.txt", "w") as f:
#     f.write(movie01 + "\n")
#     f.write(movie02 + "\n")
#     f.write(movie03 + "\n")
#     f.write(movie04 + "\n")
#     f.write(movie05 + "\n")
#     f.write(movie06 + "\n")
#     f.write(movie07 + "\n")
#     f.write(movie08 + "\n")
#     f.write(movie09 + "\n")
#     f.write(movie10 + "\n")
#     f.close()

# movie11 = "Police Academy 9"
# movie12 = "Police Academy 10"
# movie13 = "Police Academy 11"
# movie14 = "Police Academy 12"
# movie15 = "Police Academy 13"
# with open("movie-list.txt", "w") as f:
#     f.write(movie11 + "\n")
#     f.write(movie12 + "\n")
#     f.write(movie13 + "\n")
#     f.write(movie14 + "\n")
#     f.write(movie15 + "\n")
#     f.close()

# movie16 = "Police Academy 14"
# movie17 = "Police Academy 15"
# movie18 = "Police Academy 16"
# movie19 = "Police Academy 17"
# movie20 = "Police Academy 18"
# with open("movie-list.txt", "a") as f:
#     f.write(movie16 + "\n")
#     f.write(movie17 + "\n")
#     f.write(movie18 + "\n")
#     f.write(movie19 + "\n")
#     f.write(movie20 + "\n")
#     f.close()

import os
newFile = open("movie-list.txt", "r")
os.remove("C:/Users/rajib/OneDrive/Documents/tafe-python/movie-list.txt")
