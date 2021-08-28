# Word-predictor

A couple of simple python scripts that try to predict the next letter of a word you're entering.

- The `setup.py` is only needed to run once to create two directories (`.../Word-predictor/jsons/` and `.../Word-predictor/txts/`) , though you can create them yourself without any problems. 
	- To begin to actually use the scripts, it's needed to have at least one `.txt`file, inside `/txts`.
	- The longer the `.txt` files, the better. The scripts basically count the appearances of each letter after a "triad" of characters i.e. "rec", "ion", etc.

- (`text_analyzer.py`) is intended to be run from the command line, with the name of an already installed `yourfile.txt` file in the `txts` folder as the only argument (only the name of the file, not the whole path). 

	- The script will analyze the text by "triads", meaning that it will count the appearences of each letter after a given set of three previous letters ex. in "transition"... "tio" -> "n". This is done with every word. It also accounts for shorter words like "a", "an", etc, by counting the frequency of "_" empty spaces before and after the triads. The results will be saved in a json file as `yourfile_triads.py`.

	- If choosing to use the previous version (this option can be selected when running `text_analyzer.py`), The script will analyze the text and count the number of appereances of each letter according to their position in all the words of the text. The result will be saved in a json file as `yourfile_results.json`.
	
	- `$ python3 text_analyzer.py anna_karenina.txt`

- The `main_triads.py` script receives the name of a `.json` file inside de `jsons` folder ex. `yourfile_triads.json`. This file will be used to predict what you write, your input is inteded to be taken letter by letter.
	- `$ python3 main.py anna_karenina_results.json`

- The `main.py` script receives the name of a `.json` file inside de `jsons` folder ex. `yourfile_results.json`. This file will be used to predict what you write, your input is inteded to be taken letter by letter. **IMPORTANT: this script only works with `_results.json` files, which performs worse than `_triad.json` files with `main_triads.py`, I only left this functionality here in case someone might find it useful somehow.**

	- `$ python3 main.py anna_karenina_results.json`

- In the rare case that you don't have large `.txt` files lying around your computer, you can download books for free at the amazing [Project Gutenberg website](https://www.gutenberg.org).
