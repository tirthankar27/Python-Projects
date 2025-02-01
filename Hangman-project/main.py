import random
from hangman_words import word_list
from hangman_art import stages,logo
print(logo)
chosen_word = random.choice(word_list)
placeholder = list()
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
for item in placeholder:
    print(item,end="")
life=6
while life>0:
    flag=0
    print("\nLife: ",life,"/6")
    guess = input("Guess a letter: ").lower()
    for j in range(word_length):
        if chosen_word[j] == guess:
            if placeholder[j]=='_':
                placeholder[j]=guess
                flag=1
    if flag==0:
        print("The letter you choose is not in the word! You lose one life!\n")
        life-=1
        print(stages[life])
    if placeholder.count('_')==0:
        break
    for item in placeholder:
        print(item, end="")
if placeholder.count('_')==0:
    print("\nYou win")
else:
    print("\nYou lose")
    print(f"\nThe word is: {chosen_word}")
