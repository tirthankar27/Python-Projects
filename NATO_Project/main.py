import pandas as pd

data=pd.read_csv("nato_phonetic_alphabet.csv")

class NotLettersException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

nato_dict={row.letter:row.code for(index,row) in data.iterrows()}
word=""
while True:
    try:
        word=input("Enter a word: ").upper()
        if not word.isalpha():
            raise NotLettersException("Sorry, only letters in the alphabet please.")
        else:
            break
    except NotLettersException as e:
        print(e)

list_of_words=[nato_dict[letter] for letter in word]
print(list_of_words)
