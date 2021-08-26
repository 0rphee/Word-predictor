import json
import sys
import os.path as path

absolute_path = path.abspath(__file__)
file_dir = path.dirname(absolute_path)
parent_dir = path.dirname(file_dir)

txts_path = path.join(parent_dir, "txts")
jsons_path = path.join(parent_dir, "jsons")

if __name__ == "__main__":
    text_filename = sys.argv[1]
    text_path = path.join(txts_path, text_filename)
    json_file_path = path.join(jsons_path, f"{text_filename.removesuffix('.txt')}_results.json")
    triad_file_path = path.join(jsons_path, f"{text_filename.removesuffix('.txt')}_triads.json")

count = dict()
TRIAD_COUNT = dict()


def triad_counter(pure_word: str):
    processed_word = "___" + pure_word + "___"
    # new triad model, taking into account words shorter than 3 chars
    for index in range(len(processed_word[:-3])):  # "___happiness___"
        curr_triad = processed_word[index:index+3]
        curr_next_letter = processed_word[index+3]
        try:
            TRIAD_COUNT[curr_triad][curr_next_letter] += 1
        except KeyError:
            try:
                TRIAD_COUNT[curr_triad][curr_next_letter] = 1
            except KeyError:
                try:
                    TRIAD_COUNT[curr_triad] = dict()
                    TRIAD_COUNT[curr_triad][curr_next_letter] = 1
                except KeyError:
                    print("ERROR WITH DICTIONARY")
                    raise ValueError

# {"__a" : {"b": 2, etc}, "__b": {etc}, etc}
# "__a": "b", "_ab": "b", "aaa": "a"
# "b__": "_", "ba_":"_", "baa": "_"

# ___happines s ___
# 01234567891011
# len = 9


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


def process_line(line: str, use_index_count: str) -> list:
    line = line.replace("\n", "").split()
    newline = [process_word(word, use_index_count) for word in line]
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


def process_word(word: str, use_index_count: str) -> str:
    if word.isnumeric():
        return ""
    else:
        word = word.lower()
        word = remove_undesired_chars(word)
        if use_index_count == "y":
            add_count(word)
        if len(word) > 0:
            triad_counter(word)
        return word


def order_dict(dictionary: dict) -> dict:
    ordered_count = {}
    for index, dicty in dictionary.items():
        dicty = {key: value for key, value in sorted(dicty.items())}
        ordered_count[index] = dicty
    return ordered_count


def main(count: dict):
    use_index_count = input("Do you want to use indices to create json? y/n")
    with open(text_path, "r") as file:
        lines = iter(file.readlines())
        for line in lines:
            line = process_line(line, use_index_count)
    count = order_dict(count)
    if use_index_count == "y":
        with open(json_file_path, "w") as file:
            json.dump(count, file, indent=4)
    with open(triad_file_path, "w") as file:
        json.dump(TRIAD_COUNT, file, sort_keys=True, indent=4)


if __name__ == "__main__":
    main(count)
