from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")

def game():
    print("I'm thinking of a number between 1 and 100.")
    number=random.randint(1,100)
    level=input("Choose a difficulty. Type 'easy' or 'hard': ")
    flag=False
    if level == 'easy':
        for i in range(0,10):
            print(f"You have {10 - i} attempts remaining to guess the number")
            choice=int(input("Make a guess: "))
            if choice == number:
                flag=True
                break
            elif choice <= number - 10:
                print("Too Low")
                print("Guess again")
            elif choice >= number + 10:
                print("Too High")
                print("Guess again")
            elif choice <= number:
                print("Low")
                print("Guess again")
            elif choice >= number:
                print("High")
                print("Guess again")
    elif level=='hard':
        for i in range(0,5):
            print(f"You have {5 - i} attempts remaining to guess the number")
            choice=int(input("Make a guess: "))
            if choice == number:
                flag=True
                break
            elif choice <= number - 10:
                print("Too Low")
                print("Guess again")
            elif choice >= number + 10:
                print("Too High")
                print("Guess again")
            elif choice <= number:
                print("Low")
                print("Guess again")
            elif choice >= number:
                print("High")
                print("Guess again")
    if flag:
        print(f"You guessed the correct number: {number}")
    else:
        print(f"You've run out of guesses, you lose.\nCorrect answer is {number}")

game()
