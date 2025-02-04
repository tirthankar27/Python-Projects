from art import logo
print(logo)
print("Welcome to the secret auction program.")
bidders=dict()
while True:
    name=input("What is your name?: ")
    bid=input("What's your bid?: $")
    bidders[name]=bid
    option=input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if option=='yes':
        print("\n"*50)
    elif option=='no':
        break
highest=max(bidders,key=bidders.get)
print(f"The winner is {highest} with a bid of {bidders[highest]}")
