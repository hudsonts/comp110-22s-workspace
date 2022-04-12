"""EX02 - This program is a version of wordle, but with one chance!"""

__author__ = "730509671"

answer: str = "python"
length_of_guess: int = (len(answer))
guess: str = input("What is your " + str(length_of_guess) + "-letter guess? ")
word_length: int = len(guess)
WHITE_BOX: str = "\U00002B1C" 
GREEN_BOX: str = "\U0001F7E9" 
YELLOW_BOX: str = "\U0001F7E8" 


while word_length is not len(answer):
    guess = input("That was not " + str(length_of_guess) + " letters! Try again: ")
    word_length = len(guess)

if word_length == len(answer):
    if guess == answer:
        print(GREEN_BOX * word_length)
        print("Woo! You got it!")
    else:
        index: int = 0
        emoji: str = ""
        while index <= 5:
            if guess[index] != answer[index]:
                character_contained_in_word: bool = False
                alternate_indices: int = 0
                while character_contained_in_word is not True and alternate_indices < len(answer):
                    if answer[alternate_indices] == guess[index]:
                        character_contained_in_word = True
                    else:
                        alternate_indices = alternate_indices + 1
                if character_contained_in_word is True:
                    emoji = emoji + YELLOW_BOX
                else:
                    emoji = emoji + WHITE_BOX
            else:
                emoji = emoji + GREEN_BOX
            index = index + 1
        print(emoji)
        print("Not quite. Play again soon!")