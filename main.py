#calling all files that has the functions
from standard import standard
from programmer import programmer_menu
from scientific import scientific_main
from converter import converter_menu

#userinput function
#make sure the user will enter a valid number


def correctNumber(prompt:str,valid:range):
    while True:
        try:
            userinput = input(prompt).strip()
            choice=int(userinput)
            if choice in valid:
                return choice
            print(f"Your choice {userinput} is out of range .Please enter a valid number.")
        except ValueError:
            print(f"Invalid number chose number between{valid.start} to {valid.stop-1}")
        except (EOFError, KeyboardInterrupt):
            print(f"Input canceled. Returning to menu.")
#The main menu function

def main():
    print("Welcome to Multi-Mode Calculator")
    while True:
        try:
            print(f"1. Standard Mode")
            print(f"2. Programmer Mode")
            print(f"3. Scientific Mode")
            print(f"4. Converter Mode")
            print(f"5. Exit")
            choice = correctNumber("Enter your choice: " , range(1,6))
            if choice == 1:
                print(standard())
            elif choice == 2:
                print(programmer_menu())
            elif choice == 3:
                print(scientific_main())
            elif choice == 4:
                print(converter_menu())

                again = input("\nDo you want to perform another operation? (y/n): ").lower()
                if again != 'y':
                    print("Thank you for using Multi-Mode Calculator")
                    break
        except KeyboardInterrupt:
            print(f"Input canceled. Returning to menu.")
            continue
if __name__ == "__main__":
    main()




