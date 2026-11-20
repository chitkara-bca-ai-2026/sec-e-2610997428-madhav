import math

history = []

while True:
    print("\n========================================")
    print("       UTILITY CALCULATOR")
    print("========================================")

    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (Exponentiation)")
    print("7. Square Root")
    print("8. View Calculation History")
    print("9. Exit")

    choice = input("\nEnter your choice (1-9): ")

    if choice == "9":
        print("Thank you for using the Utility Calculator!")
        break

    elif choice == "8":
        print("\n--- Calculation History ---")

        if len(history) == 0:
            print("No calculations performed yet.")
        else:
            for record in history:
                print(record)

    elif choice in ("1", "2", "3", "4", "5", "6", "7"):
        try:
            num1 = float(input("Enter first number: "))

            if choice != "7":
                num2 = float(input("Enter second number: "))

            if choice == "1":
                result = num1 + num2
                operation = f"{num1} + {num2} = {result}"

            elif choice == "2":
                result = num1 - num2
                operation = f"{num1} - {num2} = {result}"

            elif choice == "3":
                result = num1 * num2
                operation = f"{num1} * {num2} = {result}"

            elif choice == "4":
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue

                result = num1 / num2
                operation = f"{num1} / {num2} = {result}"

            elif choice == "5":
                if num2 == 0:
                    print("Error: Modulus by zero is not allowed.")
                    continue

                result = num1 % num2
                operation = f"{num1} % {num2} = {result}"

            elif choice == "6":
                result = num1 ** num2
                operation = f"{num1} ** {num2} = {result}"

            elif choice == "7":
                if num1 < 0:
                    print("Error: Cannot calculate the real square root of a negative number.")
                    continue

                result = math.sqrt(num1)
                operation = f"Square root of {num1} = {result}"

            print("\nResult:", result)


            history.append(operation)

        except ValueError:
            print("Error: Please enter valid numerical values.")

    else:
        print("Invalid choice! Please select from 1 to 9.")
