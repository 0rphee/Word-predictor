import random
import json
import sys
import os.path as path
from char_freq_counter import jsons_path

triad_filename = sys.argv[1]
triad_file_path = path.join(jsons_path, triad_filename)

with open(triad_file_path) as json_file:
    DATA: dict
    DATA = json.load(json_file)


# DATA = {int(index): content for index, content in DATA.items()}
# todo fix int values

def guess_next_letter(word: str):  # word = "___hel"
    last_triad = word[-3:]
    try:
        next_char = random.choices(list(DATA[last_triad].keys()), list(DATA[last_triad].values()))[0]
        return next_char
    except KeyError:
        print("Oh no an error")
        raise KeyError


def cycle():
    word = "___"
    while True:
        letter = input("next letter:\n")
        # stops loop
        if len(letter) == 0:
            print(f"-------------------\nyour final word is:\n{word}")
            break

        word += letter
        next_char = guess_next_letter(word)
        print(f"\nuser word:\n{word[3:]}")
        print(f"next char:\n{word[3:] + next_char}\n")


if __name__ == '__main__':
    cycle()
