import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game=list([rock,paper,scissors])
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
cpu=random.randint(0,2)
print(game[choice])
print(f"Computer choose:\n{game[cpu]}")
if choice>2:
    print("You choose an invalid number")
elif choice == cpu:
    print("Draw")
elif (choice==0 and cpu == 2) or (choice==1 and cpu==0) or (choice==2 and cpu==1):
    print("You win")
else:
    print("You lose")
