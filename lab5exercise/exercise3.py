import random


def guessing_game():
    user_guess = -1
    random_number = random.randint(0, 1000)
    while (user_guess != random_number):
        user_guess = int(input("Try to guess the number: "))
        if user_guess < random_number:
            print("increase your number")
        elif user_guess > random_number:
            print("decrease your number")
        else:
            print("You guessed the number,", random_number)


guessing_game()