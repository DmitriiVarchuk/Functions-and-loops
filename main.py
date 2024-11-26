start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for i in range(start, end + 1):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}", end="\t")
    print()

