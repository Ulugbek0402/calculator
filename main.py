import csv
from file_manager import read_csv, write_csv
from operation import add, subtract, multiply, divide


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
                result = add(a, b)
            elif choice == '2':
                result = subtract(a, b)
            elif choice == '3':
                result = multiply(a, b)
            elif choice == '4':
                result = divide(a, b)

            print(f"Result: {result}")


            result_data = [a, b, result]
            write_csv('data.csv', result_data)

        elif choice == '5':

            history = read_csv('data.csv')
            if history:
                print("\nCalculation History:")
                for row in history:
                    print(f"Operands: {row[0]} and {row[1]}, Result: {row[2]}")
            else:
                print("No calculations performed yet.")

        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
