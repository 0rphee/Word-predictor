# Word-predictor

A couple of simple python scripts that try to predict the next letter of a word you're entering.

- The first script (´char_freq_counter.py´) is intended to be run from the command line, with the name of an already installed ´yourfile.txt´ file in the ´txts´ folder as the only argument (only the name of the file, not the whole path). The script will analyze the text and count the number of appereances of each letter in according to their position in all the words of the text. The result will be saved in a json file as ´yourfile_results.json´.
	- ´$ python3 char_freq_counter.py anna_karenina.txt

- The second script receives the name of a ´.json´ file inside de ´jsons´ folder ex. ´yourfile_results json´. This file will be used to predict what you write, your input is inteded to be taken letter by letter.
	- ´$ python3 main.py anna_karenina_results.json 
