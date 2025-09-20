# Lab 8 final code
# Student name: Rajib Hossain Khan
# Student no: 20145454

# Create the list
friendsList = []
userWantsToContinue = True

print("Welcome to the friend engine!")

# Start the main loop
while userWantsToContinue:
    # Present the instructions and grab the choice
    choice = input(
        "Choices are [E] to exit, [A]dd/[D]elete a friend or [P]rint all friends: ")

    # User wants to quit
    if choice.upper() == "E":
        userWantsToContinue = False
        print("Have a nice day")

    # Print the list
    elif choice.upper() == "P":
        # ---> Write code to print the list here <---
        print(friendsList)  # printing the friend list
        continue

    # Add friend to list
    elif choice.upper() == "A":
        # ---> Write code to add to the list here <---
        # getting user input for friend name to add friend
        friendName = input("Input a name to add to the list: ")
        if friendName.strip() and friendName.isalpha():  # validating the user input
            # adding the name to the list
            friendsList.append(friendName.capitalize())
            # printing success message
            print(f"Added {friendName} to the list!")
        else:
            # printing error message
            print("You entered an invalid name, please try again.")
        continue

    # Delete from list
    elif choice.upper() == "D":
        # ---> Write code to delete from the list here <---
        # getting user input for friend name to remove friend
        removeName = input("Input a name to delete: ")
        if removeName.strip() and removeName.isalpha() and friendsList.count(removeName) > 0:  # validating the user input
            # adding the name from the list
            friendsList.remove(removeName.capitalize())
            # printing success message
            print(f"Deleted {removeName} from the list!")
        else:
            print(
                f"Could not delete there was an error: {removeName} not found in the list!")  # printing error message
        continue

    # Everything else must be invalid.
    else:
        print("You made an invalid choice")
