
students = {
    "101": {
        "Name": "Ganga",
        "Branch": "BCA AI",
        "Semester": 2,
        "Marks": [85, 90, 78]
    },
    "102": {
        "Name": "Damnn",
        "Branch": "BCA AI",
        "Semester": 1,
        "Marks": [92, 86, 95]
    },
    "103": {
        "Name": "Kaka",
        "Branch": "BCA AI",
        "Semester": 1,
        "Marks": [78, 82, 87]
    }
}


def view_students():
    print("\n--- Enrolled Student Records ---")

    for roll, student in students.items():
        print(
            f"Roll No: {roll} | Name: {student['Name']} "
            f"| Branch: {student['Branch']}"
        )
        print(
            f"| Sem: {student['Semester']} "
            f"| Marks: {student['Marks']}"
        )

    print("Total Enrolled Students:", len(students))


def search_student():
    roll = input("Enter Roll Number to search: ")

    student = students.get(roll)

    if student:
        print(f"\n[FOUND] Record for Roll No: {roll}")
        print("Name    :", student["Name"])
        print("Branch  :", student["Branch"])
        print("Semester:", student["Semester"])
        print("Marks   :", student["Marks"])
    else:
        print("[ERROR] Student record not found.")


def register_student():
    print("\n--- Register New Student ---")

    roll = input("Enter Roll Number: ")

    if roll in students:
        print("[ERROR] Roll Number already exists.")
        return

    name = input("Enter Student Name: ")
    branch = input("Enter Branch (e.g. BCA AI): ")
    semester = input("Enter Semester: ")

    if not semester.isdigit() or int(semester) < 1:
        print("[ERROR] Semester must be a positive integer.")
        return

    marks = []

    for i in range(1, 4):
        try:
            mark = int(input(f"Enter Subject {i} Marks: "))

            if mark < 0 or mark > 100:
                print("[ERROR] Marks must be between 0 and 100.")
                return

            marks.append(mark)

        except ValueError:
            print("[ERROR] Please enter valid numeric marks.")
            return

    students[roll] = {
        "Name": name,
        "Branch": branch,
        "Semester": int(semester),
        "Marks": marks
    }

    print(
        f"\n[SUCCESS] Student '{name}' "
        f"(Roll No: {roll}) registered successfully."
    )

def update_student():
    roll = input("Enter Roll Number to update: ")

    if roll not in students:
        print("[ERROR] Student record not found.")
        return

    student = students[roll]

    print(f"Current details for {student['Name']} (Roll No: {roll})")
    print("1. Branch")
    print("2. Semester")

    field = input("Choose field to update (1 for Branch, 2 for Semester): ")

    if field == "1":
        new_branch = input("Enter new Branch: ")
        student["Branch"] = new_branch
        print(f"[SUCCESS] Branch updated to '{new_branch}'.")

    elif field == "2":
        new_semester = input("Enter new Semester: ")

        if new_semester.isdigit() and int(new_semester) >= 1:
            student["Semester"] = int(new_semester)
            print(f"[SUCCESS] Semester updated to '{new_semester}'.")
        else:
            print("[ERROR] Semester must be a positive integer.")

    else:
        print("[ERROR] Invalid field choice.")


def academic_performance():
    roll = input("Enter Roll Number for Academic Performance: ")

    student = students.get(roll)

    if student is None:
        print("[ERROR] Student record not found.")
        return

    marks = student["Marks"]
    total = sum(marks)
    average = total / len(marks)

    if all(mark >= 40 for mark in marks):
        result = "PASS"
    else:
        result = "FAIL"

    print("\n========== ACADEMIC REPORT ==========")
    print(f"Student Name  : {student['Name']} (Roll: {roll})")
    print(f"Subject Marks : {marks}")
    print(f"Total Marks   : {total} / 300")
    print(f"Average Marks : {average:.2f}%")
    print(f"Final Result  : {result}")
    print("=====================================")

def delete_student():
    roll = input("Enter Roll Number to delete: ")

    student = students.pop(roll, None)

    if student is not None:
        print(
            f"[SUCCESS] Record for '{student['Name']}' "
            f"(Roll No: {roll}) deleted successfully."
        )
    else:
        print("[ERROR] Student record not found.")

while True:
    print("\n========================================")
    print("    STUDENT INFORMATION MANAGEMENT SYSTEM")
    print("========================================")
    print("\nSelect an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":
        view_students()

    elif choice == "2":
        search_student()

    elif choice == "3":
        register_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        academic_performance()

    elif choice == "6":
        delete_student()

    elif choice == "7":
        print("\nThank you for using Student Information System.")
        print("Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number from 1 to 7.")
