from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
operations={"+":add,"-":subtract,"*":mul,"/":div}
num1=int(input("What's the first number?: "))
while True:
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    num2 = int(input("What's the next number?: "))
    res = operations[operation](num1, num2)
    print(f"{float(num1)} {operation} {float(num2)} = {float(res)}")
    choice=input(f"Type 'y' to continue calculating with {res} or type 'n' to start a new calculation\n").lower()
    if choice == 'n':
        break
    elif choice == 'y':
        num1=res
