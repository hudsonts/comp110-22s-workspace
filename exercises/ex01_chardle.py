"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730509671"

five_character_word: str = input("Enter a 5-character word: ")

if int(len(five_character_word)) != 5:
    print("Error: Word must contain 5 characters")
    quit()

single_character: str = input("Enter a single character: ")
if int(len(single_character)) != 1:
    print("Error: Character must be a single character.")
    quit()

print("Searching for " + single_character + " in " + five_character_word)
instance_counter: int = 0


if five_character_word[0] == single_character:
    print(single_character + " found at index 0")
    instance_counter = instance_counter + 1
if five_character_word[1] == single_character:
    print(single_character + " found at index 1")
    instance_counter = instance_counter + 1
if five_character_word[2] == single_character:
    print(single_character + " found at index 2")
    instance_counter = instance_counter + 1
if five_character_word[3] == single_character:
    print(single_character + " found at index 3")
    instance_counter = instance_counter + 1
if five_character_word[4] == single_character:
    print(single_character + " found at index 4")
    instance_counter = instance_counter + 1


if instance_counter == 0:
    print("No instances of " + single_character + " found in " + five_character_word)
if instance_counter == 1:
    print("1 instance of " + single_character + " found in " + five_character_word)
if instance_counter > 1:
    print(str(instance_counter) + " instances of " + single_character + " found in " + five_character_word)