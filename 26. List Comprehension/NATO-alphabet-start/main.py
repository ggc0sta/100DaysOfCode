import pandas as pd
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
data = pd.read_csv("nato_phonetic_alphabet.csv")
ph_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#
# print(ph_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
ph_list = [ph_dict[letter] for letter in word]
print(ph_list)
