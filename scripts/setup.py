import os
from char_freq_counter import txts_path, jsons_path

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