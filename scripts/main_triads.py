import random
import json
import sys
import os.path as path
from setup import jsons_path, standard_chars


def guess_next_letter(word: str):  # ex. word = "___hel"
    last_triad = word[-3:]
    try:
        next_char = random.choices(list(DATA[last_triad].keys()), list(DATA[last_triad].values()))[0]
        return next_char
    except KeyError:
        print("Oh no, there's not data in your analyzed text about this text sequence, the script will return a random character")
        print("Consider using a larger text to get better results")
        return random.choice(list(standard_chars))


def cycle():
    word = "___"
    while True:
        letter = input("next letter:\n")
        # stops loop
        if len(letter) == 0:
            print(f"-------------------\nyour final word is:\n{word[3:]}")
            break
        word += letter
        next_char = guess_next_letter(word)
        print(f"\nuser word:\n{word[3:]}")
        print(f"next char:\n{word[3:] + next_char}\n")


if __name__ == '__main__':
    triad_filename = sys.argv[1]
    triad_file_path = path.join(jsons_path, triad_filename)
    with open(triad_file_path) as json_file:
        DATA: dict
        DATA = json.load(json_file)
    cycle()
