def main():
    while True:
        print("""
        Calculator menu
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        5. Show history
        6. Exit
        """)

        choice = input("Enter your choice (1-6): ")

        if choice in ['1', '2', '3', '4']:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue

            if choice == '1':
                pass
            elif choice == '2':
                pass
            elif choice == '3':
                pass
            elif choice == '4':
                pass

        elif choice == '5':
            print("\nCalculation History:")
            pass

        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
