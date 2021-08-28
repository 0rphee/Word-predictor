import os
import os.path as path

special_chars = set("éê")
standard_chars = set("qwertyuiopasdfghjklzxcvbnméê")

absolute_path = path.abspath(__file__)
file_dir = path.dirname(absolute_path)
parent_dir = path.dirname(file_dir)

txts_path = path.join(parent_dir, "txts")
jsons_path = path.join(parent_dir, "jsons")


def main():
    # creation of directories
    try:
        os.mkdir(txts_path)
        try:
            os.mkdir(jsons_path)
        except OSError:
            pass
    except OSError:
        pass
    print("The directories have been set up")


if __name__ == "__main__":
    main()
