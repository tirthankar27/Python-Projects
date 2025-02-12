from game_data import data
import random
from art import logo,vs
A=random.choice(data)
B=random.choice(data)
myPoint=0
print("\n"*20,logo)
while True:
    print(f"Compare A: {A['name']},a {A['description']}, from {A['country']}")
    print(vs)
    print(f"Compare B: {B['name']},a {B['description']}, from {B['country']}")
    hnl=input("Who has more followers? Type 'A' or 'B': ")
    if hnl == 'A':
        if A['follower_count'] > B['follower_count']:
            myPoint+=1
            print("\n" * 20, logo)
            print(f"You're right! Current score {myPoint}")
        else:
            break
    elif hnl == 'B':
        if B['follower_count'] > A['follower_count']:
            myPoint+=1
            print("\n" * 20, logo)
            print(f"You're right! Current score {myPoint}")
        else:
            break
    A=B
    B = random.choice(data)
    while A==B:
        B = random.choice(data)
print("\n" * 20, logo)
print(f"Sorry, that's wrong, Final score: {myPoint}")
