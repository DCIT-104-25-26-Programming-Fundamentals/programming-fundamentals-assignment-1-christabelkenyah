# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 2
# Topic: Conditional Logic (if / elif / else) and Functions
# =============================================================================
#
# TASK: Student Grade System
#
# Write a Python program that reads a student's score and outputs the
# corresponding letter grade based on the scale below.
#
# Grading Scale:
#   Score 80 – 100  →  Grade A
#   Score 70 – 79   →  Grade B
#   Score 60 – 69   →  Grade C
#   Score 50 – 59   →  Grade D
#   Score below 50  →  Grade F
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLES
# -----------------------------------------------------------------------------
#
#   Enter student score (0-100): 85
#   Grade: A
#
#   Enter student score (0-100): 73
#   Grade: B
#
#   Enter student score (0-100): 45
#   Grade: F
#
#   Enter student score (0-100): 110
#   Error: Score must be between 0 and 100.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST use functions (see scaffold below).
# - Validate that the score is within the range 0–100 inside get_grade().
#   If it is not, return None and let main() print the error message.
# - Use if / elif / else to determine the grade.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def add_student():
    name = input("Enter the student's name: ")
    student_id = input("Enter the student's ID: ")
    scores_ip = input("Enter the student's scores separated by spaces: ")
    scores = [float(score) for score in scores_ip.split()]
    student = {
        'name': name,
        'id': student_id,
        'scores': scores
    }
    students.append(student)
    print("Student record added successfully.")

    def display_students():
        if not students:
            print("No student records found.")
            return
        print("\nStudent Records:")
        print("-" * 50)
        for student in students:
            avverage = sum(student['scores']) / len(student['scores'])
            print(f"Name: {student['name']}
            print(f"ID: {student['id']}")
            print(f"Scores: {student['scores']}")
            print(f"Average Score: {avverage:.2f}")
            print("-" * 50)

def search_student():
    search_id = input("Enter the student's ID to search: ")
    for student in students:
        if student['id'] == search_id:
            print("\nStudent Found:")
            print(f"Name: {student['name']}")
            print(f"ID: {student['id']}")
            print(f"Scores: {student['scores']}")
            avverage = sum(student['scores']) / len(student['scores'])
            print(f"Average Score: {avverage:.2f}")
            return
    print("Student not found.")
    while True:
    print("\n===== Student Record Management System =====")
    print("1. Add Student Record")
    print("2. Display All Student Records")
    print("3. Search Student Record by ID")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_student()    elif choice == '4':
        print("Program terminated.")
        break
        else:
        print("Invalid choice. Please try again.")
