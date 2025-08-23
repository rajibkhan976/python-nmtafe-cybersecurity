# Name: Rajib Hossain Khan
# Student ID: 20145454
# Version: 202009081123

try:
    user_input = input('Enter a number 1 to 30: ')
    n = int(user_input)
    if n < 0 or n > 30:
        print(n, " is not between 0 and 31.")
    elif n == 0:
        print(n, " entered.")
    elif n >= 1 and n <= 10:
        print(n, " is larger than 0, and smaller than 11")
    elif n >= 11 and n <= 20:
        print(n, " is larger than 10, and smaller than 21")
    else:
        print(n, " is equal or over 21")
except Exception as err_msg:
    print(user_input, " is not a valid integer.")
