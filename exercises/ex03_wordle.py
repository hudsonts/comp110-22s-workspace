"""This is a program that emulates the popular word game 'wordle'."""

__author__ = "730509671"
WHITE_BOX: str = "\U00002B1C" 
GREEN_BOX: str = "\U0001F7E9" 
YELLOW_BOX: str = "\U0001F7E8" 


def contains_char(string_searched_through: str, single_character: str) -> bool:
    """This function scans through the first parameter to see if the second character is contained."""
    assert len(single_character) == 1
    character_contained_in_word: bool = False
    alternate_indices: int = 0
    while character_contained_in_word is not True and alternate_indices < len(string_searched_through):
        if string_searched_through[alternate_indices] == single_character:
            character_contained_in_word = True
        else:
            alternate_indices = alternate_indices + 1
    if character_contained_in_word is True:
        return True
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    """This function calls on the contains_char function to compare the digits of two words, then returns a wordle-style emoji string."""
    assert len(guess) == len(secret)
    if guess == secret:
        emoji = (GREEN_BOX * len(guess))
    else:
        index: int = 0
        emoji = ""
        while index < len(guess):
            if guess[index] != secret[index]:
                if contains_char(secret, guess[index]) is True:
                    emoji = emoji + YELLOW_BOX
                else:
                    emoji = emoji + WHITE_BOX
            else:
                emoji = emoji + GREEN_BOX
            index = index + 1
    return emoji


def input_guess(word_length: int) -> str:
    """This function prompts the user to input a guess based on a number of characters promped by the program developer."""
    user_guess: str = input("Enter a " + str(word_length) + " character word: ")
    while len(user_guess) != word_length:
        user_guess = input("That wasn't " + str(word_length) + " chars! Try again: ")
    return user_guess
    

def main() -> None: 
    """The entrypoint of the program and main game loop."""
    wordle: str = "wordle"
    turn: int = 1
    guess: str = ""
    while turn < 7 and guess != wordle:
        print("=== Turn " + str(turn) + "/6 ===")
        guess = input_guess(len(wordle))
        print(emojified(guess, wordle))
        turn = turn + 1
        if turn == 7: 
            print("X/6 - Sorry, try again tomorrow!")
    if guess == wordle:
        print("You won in " + str(turn - 1) + "/6 turns!")
