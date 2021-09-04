"""Counting letters in a string."""

__author__ = "730329962"

letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
matches: int = 0
letter_counter: int = 0
word_length: int = len(word)

while letter_counter < word_length:
    if (word[letter_counter]) == letter:
        matches = matches + 1
    letter_counter = letter_counter + 1

print("Count: " + str(matches))