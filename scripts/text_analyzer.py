import json
import sys
import os.path as path
from setup import txts_path, jsons_path, special_chars, standard_chars


def triad_counter(pure_word: str):
    processed_word = "___" + pure_word + "___"
    for index in range(len(processed_word[:-3])):  # ex. "___happiness___"
        curr_triad = processed_word[index:index+3]
        curr_next_letter = processed_word[index+3]
        try:
            TRIAD_COUNT[curr_triad][curr_next_letter] += 1
        except KeyError:
            try:
                TRIAD_COUNT[curr_triad][curr_next_letter] = 1
            except KeyError:
                TRIAD_COUNT[curr_triad] = dict()
                TRIAD_COUNT[curr_triad][curr_next_letter] = 1


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


def process_line(line: str, use_index_count: str):
    line = line.replace("\n", "").split()
    [process_word(word, use_index_count) for word in line]


def remove_undesired_chars(word: str) -> str:
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


def main(inner_count: dict):
    use_index_count = input("Do you want to create a json with character frequency by position in the word? y/n")
    with open(text_path, "r") as file:
        lines = iter(file.readlines())
        for line in lines:
            process_line(line, use_index_count)
    inner_count = order_dict(inner_count)
    if use_index_count == "y":
        with open(json_file_path, "w") as file:
            json.dump(inner_count, file, sort_keys=True, indent=4)
    with open(triad_file_path, "w") as file:
        json.dump(TRIAD_COUNT, file, sort_keys=True, indent=4)


if __name__ == "__main__":
    text_filename = sys.argv[1]
    text_path = path.join(txts_path, text_filename)
    json_file_path = path.join(jsons_path, f"{text_filename.removesuffix('.txt')}_results.json")
    triad_file_path = path.join(jsons_path, f"{text_filename.removesuffix('.txt')}_triads.json")
    count = dict()
    TRIAD_COUNT = dict()
    main(count)
