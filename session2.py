"""
@Time ： 2024-09-13
@Auth ： Adam Lyu
"""

# 1. the difference of sets Aliasing
# Creating a set
original_set = {1, 2, 3, 4, 5}
# Aliasing the original set
alias_set = original_set
# Modifying the alias set
alias_set.add(6)
# Printing both sets to show that they both reflect the change
print("Original Set:", original_set)
print("Alias Set:", alias_set)


# the difference between append and extend
# Create an initial list
my_list = [1, 2, 3]

# Use append() to add an element (a list)
my_list.append([4, 5])
print("After append:", my_list)

# Use extend() to add elements (expand the list)
my_list.extend([6, 7])
print("After extend:", my_list)

# After append: [1, 2, 3, [4, 5]]
# After extend: [1, 2, 3, [4, 5], 6, 7]

# 3. without using elif
num = 1
if num > 0:
    print("Positive number")
else:
    if num == 0:
        print("Zero")
    else:
        print("Negative number")

# 4.
# Create a dictionary to store students and their grades
# students_grades = {}
#
#
# Function 1: Batch input of student names
def add_students():
    while True:
        name = input("Enter student name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        students_grades[name] = None  # Initial grade set to None


# Function 2: Input grades for existing students
def input_grades():
    if not students_grades:
        print("No students available. Please add students first.")
        return
    for student in students_grades:
        while True:
            try:
                grade = float(input(f"Enter grade for {student}: "))
                students_grades[student] = grade
                break
            except ValueError:
                print("Invalid input, please enter a number.")


# Function 3: Output a student's grade based on their name
def get_student_grade():
    name = input("Enter the name of the student to get the grade: ")
    if name in students_grades:
        grade = students_grades[name]
        if grade is not None:
            print(f"{name}'s grade is: {grade}")
        else:
            print(f"{name} does not have a grade yet.")
    else:
        print(f"No student found with the name {name}.")


# Main function with a menu to choose the operation
def main():
    while True:
        print("\nChoose an option:")
        print("1. Add students")
        print("2. Input grades")
        print("3. Get a student's grade")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_students()
        elif choice == '2':
            input_grades()
        elif choice == '3':
            get_student_grade()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()


# 5 the difference between global and local variable
# Global variable
x = 10

def my_function():
    # Local variable
    x = 5
    print("Inside the function, x:", x)  # Prints the local variable x

my_function()

# Prints the global variable x
print("Outside the function, x:", x)


# 5. OOB

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_grades(self):
        return self.grades


class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self):
        name = input("Enter the student's full name: ")
        if name not in self.students:
            self.students[name] = Student(name)
            print(f"Student {name} added.")
        else:
            print(f"Student {name} already exists.")

    def add_grade(self):
        name = input("Enter the student's full name to add a grade: ")
        if name in self.students:
            try:
                grade = float(input(f"Enter the grade for {name}: "))
                self.students[name].add_grade(grade)
                print(f"Grade {grade} added for {name}.")
            except ValueError:
                print("Invalid grade. Please enter a number.")
        else:
            print(f"Student {name} not found.")

    def print_student_grades(self):
        name = input("Enter the student's full name to print grades: ")
        if name in self.students:
            grades = self.students[name].get_grades()
            if grades:
                print(f"{name}'s grades: {', '.join(map(str, grades))}")
            else:
                print(f"{name} has no grades.")
        else:
            print(f"Student {name} not found.")

    def menu(self):
        while True:
            print("\n1. Add student")
            print("2. Add grade")
            print("3. Print student grades")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.add_grade()
            elif choice == '3':
                self.print_student_grades()
            elif choice == '4':
                print("Exiting program.")
                break
            else:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    manager = StudentManager()
    manager.menu()
