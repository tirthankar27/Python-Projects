from art import logo
import random

def play_game():
    print("\n" * 20)
    print(logo)
    dealer_score = 0

    card1 = my_cards[random.choice(list(my_cards.keys()))]
    my_list.append(card1)
    card2 = my_cards[random.choice(list(my_cards.keys()))]
    my_list.append(card2)
    my_score = card1 + card2

    dealer_card = my_cards[random.choice(list(my_cards.keys()))]
    dealer_score += dealer_card
    dealers_list.append(dealer_card)

    print(f"You got cards {my_list}: Your current score is {my_score}")
    print(f"Dealer got card {dealers_list}: Dealer current score {dealer_score}")

    if my_score == 21:
        print("Blackjack! You win 🎉")
        return
    elif my_score > 21:
        print("Bust! You lose 😢")
        return
    else:
        while my_score < 21:
            choice = input("Do you want a card? Type 'y' to choose or 'n' to pass: ").lower()
            if choice == 'n':
                break
            card2 = my_cards[random.choice(list(my_cards.keys()))]
            my_score += card2
            my_list.append(card2)

            print(f"You got cards {my_list}: Your current score is {my_score}")
            print(f"Dealer got card {dealers_list}: Dealer current score {dealer_score}")

            if my_score == 21:
                print("Blackjack! You win 🎉")
                break
            elif my_score > 21:
                print("Bust! You lose 😢")
                break
        if my_score < 21:
            while dealer_score < 17:
                dealer_card = my_cards[random.choice(list(my_cards.keys()))]
                dealer_score += dealer_card
                dealers_list.append(dealer_card)

            print(f"You got cards {my_list}: Your current score is {my_score}")
            print(f"Dealer got card {dealers_list}: Dealer current score {dealer_score}")

            if my_score > dealer_score and my_score < 22 or dealer_score > 21:
                print("You win 🎉")
            elif my_score < dealer_score:
                print("Sorry, you lose 😢")
            else:
                print("It's a draw 🤝")
            return

my_cards={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}
game=input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
my_list=list()
dealers_list=list()

while game=='y':
    play_game()
    game=input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
    my_list.clear()
    dealers_list.clear()
