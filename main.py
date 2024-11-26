def count_digits(number):
    return len(number)


def sum_digits(number):
    return sum(int(digit) for digit in number)


def average_digits(number):
    total_sum = sum_digits(number)
    return total_sum / len(number)


def count_zeros(number):
    return number.count("0")


user_number = None

while True:
    print("\nMenu:")
    print("1. Enter a number")
    print("2. Count the number of digits")
    print("3. Calculate the sum of the digits")
    print("4. Calculate the arithmetic mean of the digits")
    print("5. Count the number of zeros")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        user_number = input("Enter a number: ")
        print(f"You entered the number: {user_number}")

    elif choice == "2":
        if user_number is not None:
            print(f"The number of digits in {user_number}: {count_digits(user_number)}")
        else:
            print("Please enter a number first (option 1).")

    elif choice == "3":
        if user_number is not None:
            print(f"The sum of the digits in {user_number}: {sum_digits(user_number)}")
        else:
            print("Please enter a number first (option 1).")

    elif choice == "4":
        if user_number is not None:
            print(f"The arithmetic mean of the digits in {user_number}: {average_digits(user_number):.2f}")
        else:
            print("Please enter a number first (option 1).")

    elif choice == "5":
        if user_number is not None:
            print(f"The number of zeros in {user_number}: {count_zeros(user_number)}")
        else:
            print("Please enter a number first (option 1).")

    elif choice == "6":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice, please try again.")

def print_chess_board(cell_size, board_size=8):
    for row in range(board_size):
        for i in range(cell_size):
            for col in range(board_size):
                if (row + col) % 2 == 0:
                    print("*" * cell_size, end="")
                else:
                    print("-" * cell_size, end="")
            print()


cell_size = int(input("Enter the cell size: "))
print_chess_board(cell_size)
