#!/usr/bin/env python3

# Created by: Brian Musembi
# Created on: 03 May 2021
# This program allows the user to guess the correct number

import random


def main():
    # this function allows the user to guess the correct number
    answer = random.randint(0, 9)  # a number between 1 and 100

    # input
    guess = int(input("Enter the number between 0 - 9: "))

    # process & output
    if guess == answer:
        print("You guessed correct!")
    else:
        print('Incorrect, the number was: {0}'.format(answer))
        print("")
        print("Done.")


if __name__ == "__main__":
    main()
