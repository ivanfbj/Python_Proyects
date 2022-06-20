"""
source:
https://youtu.be/8ext9G7xspg?t=414
Guess the Number
The objective of this project is to develop a software for Guess the number, create number for computer.
This proyect will building with functions, loop while, conditionals and user inputs.
"""
import random


def guess(number):
    random_number = random.randint(1, number)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {number}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low')
        elif guess > random_number:
            print('Sorry, guess again. Too high')
    print(f'Yay, congrats. You have guessed the number {random_number} correctly.')


if __name__ == "__main__":
    guess(10)
