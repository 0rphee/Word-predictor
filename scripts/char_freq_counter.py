import json
import os
import sys
import os.path as path

text_filename = sys.argv[1]

absolute_path = path.abspath(__file__)
file_dir = path.dirname(absolute_path)
parent_dir = path.dirname(file_dir)

txts_path = path.join(parent_dir, "txts")
jsons_path = path.join(parent_dir, "jsons")

text_path = path.join(txts_path, text_filename)
json_file_path = path.join(jsons_path, f"{text_filename.removesuffix('.txt')}_results.json")

count = dict()


def add_count(word: str):
    for index, char in enumerate(word):
        if index in count:
            pass
        else:
            count[index] = dict()
        if char in count[index]:
            count[index][char] += 1
        else:
            count[index][char] = 1


def process_line(line: str) -> list:
    line = line.replace("\n", "").split()
    newline = [process_word(word) for word in line]
    return newline


def remove_undesired_chars(word: str) -> str:
    special_chars = set("éê")
    standard_chars = set("qwertyuiopasdfghjklzxcvbnméê")
    acceptable_chars = special_chars.union(standard_chars)
    # characters = set(""",;.:-_{[}]´¨+*!"#$%&/()=?'¿¡“’""")
    for char in set(word):
        if char not in acceptable_chars:
            word = word.replace(char, "")
        if char in special_chars:
            word = word.replace(char, "e")
    return word


def process_word(word: str) -> str:
    if word.isnumeric():
        return ""
    else:
        word = word.lower()
        word = remove_undesired_chars(word)
        add_count(word)
        return word


def order_dict(dictionary: dict) -> dict:
    ordered_count = {}
    for index, dicty in dictionary.items():
        dicty = {key: value for key, value in sorted(dicty.items())}
        ordered_count[index] = dicty
    return ordered_count


def main(count: dict):
    with open(text_path, "r") as file:
        lines = iter(file.readlines())
        for line in lines:
            line = process_line(line)
    count = order_dict(count)
    with open(json_file_path, "w") as file:
        json.dump(count, file, indent=4)


if __name__ == "__main__":
    main(count)
