import random

def multiplication_test(level, questions):
    correct_answers = 0

    for _ in range(questions):
        if level == 1:
            num1, num2 = random.randint(1, 5), random.randint(1, 5)
        elif level == 2:
            num1, num2 = random.randint(1, 10), random.randint(1, 10)
        elif level == 3:
            num1, num2 = random.randint(1, 15), random.randint(1, 15)
        user_answer = int(input(f"How much will be {num1} * {num2}? "))

        if user_answer == num1 * num2:
            print("Right")
            correct_answers += 1
        else:
            print(f"Wrong. Correct answer: {num1 * num2}")

    print(f"\nyou gave {correct_answers} correct answers with{questions}.")
    percentage = (correct_answers / questions) * 100
    if percentage == 100:
        print("A+")
    elif percentage >= 75:
        print("B+")
    elif percentage >= 50:
        print("F-")
    else:
        print("Not satisfactory. You still need to practice.")


print("Choose difficulty level:")
print("1. Easy (numbers 1 to 5)")
print("2. Average (numbers from 1 to 10)")
print("3. Hard (numbers from 1 to 15)")

level = int(input("Enter the level number (1-3): "))
questions = int(input("How many questions do you want to answer? "))

multiplication_test(level, questions)