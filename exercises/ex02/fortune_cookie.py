"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730329962"

from random import randint

print("Your fortune cookie says...")

x = randint(1, 4)

if x == 1:
    print("Something surprising will happen today.")
else:
    if x == 2:
        print("Today is going to be the best day of the week.")
    else: 
        if x == 3:
            print("Walk backwards through doors for good luck today.")
        else:
            if x == 4:
                print("This week will be important for the future.")
print("Now, go spread positive vibes!")