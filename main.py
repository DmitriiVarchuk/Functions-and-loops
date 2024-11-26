def print_diamond(size):
    for i in range(size):
        print(" " * (size - i - 1) + "*" * (2 * i + 1))

    for i in range(size - 2, -1, -1):
        print(" " * (size - i - 1) + "*" * (2 * i + 1))


size = int(input("Enter the size of the diamond: "))
print_diamond(size)
