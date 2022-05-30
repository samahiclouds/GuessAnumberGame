# importing the random module
row = "******WELCOME TO THE******"
print(row.center(200))
row2 = "*****GUESS A NUMBER****"
print(row2.center(200))
row3 = "********GAME********"
print(row3.center(200))

import random

incorrect_answers = []

user_name = input("What's your name?")
print(f"Hello {user_name}")
# Assigning a variable
x = random.randint(0, 100)

# print(x)

while (True):
    number = int(input(f"enter a number between 0 and 100!"))
    if number not in range(0, 101):
        print("invalid number, please key in number between 0 and 10!")
    elif number < x:
        print("too low try again")
        incorrect_answers.append(number)

    elif number > x:
        print("too high try again!")
        incorrect_answers.append(number)

    elif number == x:
        print("Good guessing!")
        print("Your incorrect guesses were:", incorrect_answers)
        tries = len(incorrect_answers)
        print(f"It took you {tries} tries to get the correct answer")
        row4 = ("**********PRESS ENTER TO EXIT OR CLICK RUN TO PLAY AGAIN**********")
        print(row4.center(200))
        break