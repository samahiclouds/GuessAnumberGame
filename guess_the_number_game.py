
# Displaying the welcome screen.
row = "******WELCOME TO THE******"
print(row.center(200))
row2 = "*****GUESS A NUMBER****"
print(row2.center(200))
row3 = "********GAME********"
print(row3.center(200))

# Importing the random module.
import random

# Creating an empty list to store incorrect answers.
incorrect_answers = []

# Requesting & Displaying the player's name.
user_name = input("What's your name?")
print(f"Hello {user_name}")

# Assigning the random number to a variable & restricting the range between 0 to 100.
x = random.randint(0, 100)


# Creating a while loop to start the game.
while (True):
    # Requesting the player to guess a number and enter it.
    number = int(input(f"enter a number between 0 and 100!"))

    # Conditional statement to in case of number entered is out of range to ask player to renter a valid number.
    if number not in range(0, 101):
        print("invalid number, please key in number between 0 and 10!")

    # Statement to indicate that number is lower than random number and store the incorrect answer in the list.
    elif number < x:
        print("too low try again")
        incorrect_answers.append(number)

    # Statement to indicate that number is higher than random number and store the incorrect answer in the list.
    elif number > x:
        print("too high try again!")
        incorrect_answers.append(number)

    # Statement to indicate that the number is correct, then it prints a list of incorrect answers.
    elif number == x:
        print("Good guessing!")
        print("Your incorrect guesses were:", incorrect_answers)

        # Creating a variable for the number of tries the player took to the correct answer, then display the results.
        tries = len(incorrect_answers)
        print(f"It took you {tries} tries to get the correct answer")

        # Instruction on how to exit the game or play again.
        row4 = ("**********PRESS ENTER TO EXIT OR CLICK RUN TO PLAY AGAIN**********")
        print(row4.center(200))

        # Exiting the loop.
        break