def programmer_menu() :
    while True:
        choice = input("Enter 1 if you want conversation calculator\n Enter 2 if you want Bitwise calculator:")
        if choice == '1':
            return conversions()
        elif choice == '2':
            return bitwise()
        else:
            print("\n\nError: Please enter 1 or 2.\n\n\n\n\n\n\n")
            continue
def bitwise():
    while True:
        try:

            operator = input("Enter the operation that you want to use: ")
            if operator == "&":
                integer1, integer2 = eval(input("Enter two integers that you want to apply AND operator respectively, and split it by commas: "))
                print("The AND of integer1 and integer2 is: ", end="")
                return integer1 & integer2

            elif operator == "|":
                integer1, integer2 = eval(input("Enter two integers that you want to apply OR operator respectively, and split it by commas: "))
                return integer1 | integer2
            elif operator == "^":
                integer1, integer2 = eval(input(
                    "Enter two integers that you want to apply XOR operator respectively, and split it by commas: "))
                print("The XOR of integer1 and integer2 is: ", end="")
                return integer1 ^ integer2
            elif operator == "<<":
                integer1, integer2 = eval(input(
                    "Enter two integers that you want to apply left shift operator respectively, and split it by commas: "))
                print("The left shift of integer1 and integer2 is: ", end="")
                return integer1 << integer2
            elif operator == ">>":
                integer1, integer2 = eval(input(
                    "Enter two integers that you want to apply right shift operator respectively, and split it by commas: "))
                print("The right shift of integer1 and integer2 is: ", end="")
                return integer1 >> integer2
            elif operator == "~":
                integer1 = eval(input(
                    "Enter the integer that you want to apply NOT operator: "))
                print("The NOT of the integer is: ", end="")

                return ~integer1
            else:
                print("You Enter wrong operator.")
        except ValueError as e:
            print("The problem is: ", end="")
            return e
        except NameError as e:
            print("The Values that you are enter is not correct\n The python error description is: ", end="")
            return e
def conversions():
    while True:
        print(
            "Enter 1 - Decimal to Binary\nEnter 2 - Decimal to Octal\nEnter 3 - Decimal to Hexadecimal\nEnter 4 - Binary to Decimal\nEnter 5 - Octal to Decimal\nEnter 6 - Hexadecimal to Decimal")
        cv = input("Enter a number: ")
        if cv == "1":
            return dtb()
        elif cv == "2":
            return dto()
        elif cv == "3":
            return dth()
        elif cv == "4":
            return btd()
        elif cv == "5":
            return otd()
        elif cv == "6":
            return htd()
        else:
            print("\n\nInvalid input, please try again\n\n")
            continue

def dtb():
    try:
        dtb1 = int(input("Enter decimal number: "))
        result = f"binary: {bin(dtb1)[2:]}"
        return result
    except ValueError:
        return "Error: Please enter a valid integer."

def dto():
    try:
        dto1 = int(input("Enter decimal number: "))
        result = f"octal: {oct(dto1)[2:]}"
        return result
    except ValueError:
        return "Error: Please enter a valid integer."

def dth():
    try:
        dth1 = int(input("Enter decimal number: "))
        result = f"hexadecimal: {hex(dth1)[2:]}"
        return result
    except ValueError:
        return "Error: Please enter a valid integer."

def btd():
    try:
        btd1 = input("Enter binary number: ")
        result = f"decimal: {int(btd1, 2)}"
        return result
    except ValueError:
        return "Error: Please enter a valid binary number."

def otd():
    try:
        otd1 = input("Enter octal number: ")
        result = f"decimal: {int(otd1, 8)}"
        return result
    except ValueError:
        return "Error: Please enter a valid octal number."

def htd():
    try:
        htd1 = input("Enter hexadecimal number: ")
        result = f"decimal: {int(htd1, 16)}"
        return result
    except ValueError:
        return "Error: Please enter a valid hexadecimal number."

if __name__ == "__main__":
    programmer_menu()
