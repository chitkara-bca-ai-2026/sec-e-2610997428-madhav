from datetime import datetime

def add_log():
    logs = []

    entry = input("Enter log entry: ")

    logs.append(entry)

    with open("daily_log.txt", "a") as file:
        for log in logs:
            file.write(str(datetime.now()) + " - " + log + "\n")

    print("Log added successfully!")


def display_log():
    with open("daily_log.txt", "r") as file:
        print("\n===== DAILY LOG BOOK =====")
        print(file.read())


while True:
    print("\n1. Add Log Entry")
    print("2. Display Complete Log")
    print("3. Exit")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        add_log()

    elif choice == "2":
        display_log()

    elif choice == "3":
        print("Thank you! Goodbye.")
        break

    else:
        print("Invalid Choice!")
