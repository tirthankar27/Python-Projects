print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")
print("You're at a cross road. Where do you want to go?")
choice=input("\tType \"Left\" or \"Right\"\n ")
if choice == 'Left':
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice = input("\tType \"Wait\" to wait for a boat. Type \"Swim\" to swim across.\n")
    if choice == 'Wait':
        print("You arrive at island unharmed. There is a house with 3 doors.")
        choice=input("\tOne red, one yellow and one blue. Which colour do you choose?\n")
        if choice == 'Red':
            print("Burned by fire. Game Over.")
        elif choice == 'Blue':
            print("Eaten by beasts. Game Over.")
        elif choice == 'Yellow':
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")