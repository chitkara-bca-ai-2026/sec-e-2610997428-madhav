print("========================================")
print("       SCHOOL RESULT PROCESSING")
print("========================================")


student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")

# Input marks for 5 subjects
marks = []

print("\n--- Enter Marks for 5 Subjects (0-100) ---")

for i in range(1, 6):
    mark = int(input(f"Enter marks for Subject {i}: "))

    
    if mark < 0 or mark > 100:
        print("Error: Marks must be between 0 and 100.")
        exit()

    marks.append(mark)


failed = False

for mark in marks:
    if mark < 40:
        failed = True


total_marks = sum(marks)
percentage = (total_marks / 500) * 100

if failed:
    result = "FAIL"
    grade = "F"
    remark = "Failed in one or more subjects"
else:
    result = "PASS"

    if percentage >= 90:
        grade = "A+"
        remark = "Outstanding"
    elif percentage >= 80:
        grade = "A"
        remark = "Excellent"
    elif percentage >= 70:
        grade = "B"
        remark = "Very Good"
    elif percentage >= 60:
        grade = "C"
        remark = "Good"
    elif percentage >= 50:
        grade = "D"
        remark = "Satisfactory"
    elif percentage >= 40:
        grade = "E"
        remark = "Pass"
    else:
        grade = "F"
        remark = "Fail"

print("\n========================================")
print("           STUDENT REPORT CARD")
print("========================================")
print(f"Student Name : {student_name}")
print(f"Roll Number  : {roll_number}")
print("----------------------------------------")
print(f"Total Marks  : {total_marks:.1f} / 500.0")
print(f"Percentage  : {percentage:.2f}%")
print(f"Result       : {result}")
print(f"Grade        : {grade}")
print(f"Remarks      : {remark}")
print("========================================")
