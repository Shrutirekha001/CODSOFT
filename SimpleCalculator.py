def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Undefined (division by zero)"
    return x / y
while True:
    print("This are the Options:")
    print("Enter 'add' for addition")
    print("Enter 'sub' for subtraction")
    print("Enter 'mul' for multiplication")
    print("Enter 'div' for division")
    print("Enter 'quit' to end the program")
    user_input = input("Choose one option : ")

    if user_input == "quit":
        break
    if user_input in ("add", "sub", "mul", "div"):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if user_input == "add":
            print("The addition of", x,"and",y, "is :", add(x, y))
            print("")
        elif user_input == "sub":
            print("The subtraction of", x,"and",y, "is :", subtract(x, y))
            print("")
        elif user_input == "mul":
            print("The multiplication of", x,"and",y, "is :", multiply(x, y))
            print("")
        elif user_input == "div":
            print("The division of", x,"and",y, "is :", divide(x, y))
            print("")
    else:
        print("Invalid Input")
        print("")