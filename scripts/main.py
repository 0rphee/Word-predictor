import random
import json
import sys
import os.path as path
from setup import jsons_path, standard_chars


def guess_next_char(word: str) -> str:
    next_index = len(word)
    try:
        chars = DATA[next_index]
        chars = {key: int(value) for key, value in sorted(chars.items(), key=lambda x: -int(x[1]))}
        next_char = random.choices(list(chars.keys()), list(chars.values()))[0]
        return next_char
    except KeyError:
        print("Oh no, there's not data in your analyzed text about a word this long, the script will return a random character")
        print("Consider using a larger text to get better results")
    return random.choice(list(standard_chars))


def cycle():
    word = ""
    while True:
        letter = input("next letter:\n")
        if len(letter) == 0:
            print(f"-------------------\nyour final word is:\n{word}")
            break
        word += letter
        next_char = guess_next_char(word)
        print(f"user word:\n{word}")
        print(f"next char:\n{word + next_char}")

if __name__ == '__main__':
    json_filename = sys.argv[1]
    json_file_path = path.join(jsons_path, json_filename)
    with open(json_file_path) as json_file:
        DATA: dict
        DATA = json.load(json_file)
    DATA = {int(index): content for index, content in DATA.items()}
    cycle()
