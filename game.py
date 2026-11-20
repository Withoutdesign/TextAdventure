# Translated from Lua guessing game
import random

low = 1
high = 100

randomNumber = random.randint(1, 100)

won = False

def game():
    global low, high, won
    
    while won == False:
        print(f"<Brother> I'm thinking of a number between {low}-{high}")

        try:
            guess = int(input())

            if guess < low or guess > high:
                print("\n-> *Out of Range* -Guess between the range-")

            elif guess == randomNumber:
                won = True
                break

            elif guess < randomNumber:
                print("\n-> *Too Low* -Try Again!-")
                low = guess + 1

            elif guess > randomNumber:
                print("\n-> *Too High* -Try Again!-")
                high = guess - 1

        except ValueError:
            print("\n-> *Invalid Input* -Enter a valid number-")