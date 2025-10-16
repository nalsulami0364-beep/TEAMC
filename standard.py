import math

# Here function to perform addition
def add(x,y):
    return x + y

# Here function to perform subtraction
def subtract(x,y):
    return x - y

# Here function to perform multiplication
def multiply(x,y):
    return x * y

# Here function to perform division with zero division error
def divide(x,y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error, you can't divide by zero."
    
# Here function to perform module operation
def modulo(x,y):
    try:
        return x % y  
    except ZeroDivisionError:
        return "Error, you can't divide by zero."
 
 # Here function to perform exponentiation 
def exponentiate(x,y):
    return x ** y

# Here function to perform square root with negative number
def SquareRoot(x):
    if x < 0:
        return "Error, square root of negative number is Unspported."
    return math.sqrt(x)

# Here function to perform reciprocal 1/x
def reciprocal(x):
    if x == 0:
        return "Error, cannot find reciprocal of 0"
    return 1 / x

# Here function to calculate percentage 
def percentage(x,percent):
    
    return (x * percent) / 100

def standard():
    print("Started program\n")
    while True:
        print("Standard Calculater")
        print("#1 Add")
        print("#2 subtract")
        print("#3 Multiply")
        print("#4 Divide")
        print("#5 Modulo")
        print("#6 Exponentiate")
        print("#7 Square Root")
        print("#8 Reciprocal")
        print("#9 Percentage")
        print("#10 Exit")

        try:
            choice = int(input("Enter any operation you want from 1 to 10:"))
        except ValueError:
            print("Error, please try again and enter right choice")
            continue

        if choice == 10:
            print("Exiting Standard Calucalter")
            break

        if choice == 1:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result = ",add(x,y))

        elif choice == 2:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result = ",subtract(x,y))

        elif choice == 3:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result = ",multiply(x,y))

        elif choice == 4:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result = ",divide(x,y))

        elif choice == 5:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result = ",modulo(x,y))

        elif choice == 6:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result = ",exponentiate(x,y))

        elif choice == 7:
            x = float(input("Enter a number: "))
            print(f"Result = ",SquareRoot(x))

        elif choice == 8:
            x = float(input("Enter a number: "))
            print(f"Result = ",reciprocal(x))

        elif choice == 9:
            x = float(input("Enter a number: "))
            percent = float(input("Enter percentage: "))
            print(f"Result = ",percentage(x,percent))

        else:
            print("Invalid choice, try again !")
standard()