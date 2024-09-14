"""
@Time ： 2024-09-13
@Auth ： Adam Lyu
"""

# # 1.
# # Creating a set
# original_set = {1, 2, 3, 4, 5}
# # Aliasing the original set
# alias_set = original_set
# # Modifying the alias set
# alias_set.add(6)
# # Printing both sets to show that they both reflect the change
# print("Original Set:", original_set)
# print("Alias Set:", alias_set)
#
#
#
# # Create an initial list
# my_list = [1, 2, 3]
#
# # Use append() to add an element (a list)
# my_list.append([4, 5])
# print("After append:", my_list)
#
# # Use extend() to add elements (expand the list)
# my_list.extend([6, 7])
# print("After extend:", my_list)
#
# # After append: [1, 2, 3, [4, 5]]
# # After extend: [1, 2, 3, [4, 5], 6, 7]
#
#
# if num > 0:
#     print("Positive number")
# else:
#     if num == 0:
#         print("Zero")
#     else:
#         print("Negative number")

# Create a dictionary to store students and their grades
# students_grades = {}
#
#
# # Function 1: Batch input of student names
# def add_students():
#     while True:
#         name = input("Enter student name (or type 'done' to finish): ")
#         if name.lower() == 'done':
#             break
#         students_grades[name] = None  # Initial grade set to None
#
#
# # Function 2: Input grades for existing students
# def input_grades():
#     if not students_grades:
#         print("No students available. Please add students first.")
#         return
#     for student in students_grades:
#         while True:
#             try:
#                 grade = float(input(f"Enter grade for {student}: "))
#                 students_grades[student] = grade
#                 break
#             except ValueError:
#                 print("Invalid input, please enter a number.")
#
#
# # Function 3: Output a student's grade based on their name
# def get_student_grade():
#     name = input("Enter the name of the student to get the grade: ")
#     if name in students_grades:
#         grade = students_grades[name]
#         if grade is not None:
#             print(f"{name}'s grade is: {grade}")
#         else:
#             print(f"{name} does not have a grade yet.")
#     else:
#         print(f"No student found with the name {name}.")
#
#
# # Main function with a menu to choose the operation
# def main():
#     while True:
#         print("\nChoose an option:")
#         print("1. Add students")
#         print("2. Input grades")
#         print("3. Get a student's grade")
#         print("4. Exit")
#
#         choice = input("Enter your choice: ")
#
#         if choice == '1':
#             add_students()
#         elif choice == '2':
#             input_grades()
#         elif choice == '3':
#             get_student_grade()
#         elif choice == '4':
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice. Please try again.")
#
# # Run the program
# main()
#
#
# # Global variable
# x = 10
#
# def my_function():
#     # Local variable
#     x = 5
#     print("Inside the function, x:", x)  # Prints the local variable x
#
# my_function()
#
# # Prints the global variable x
# print("Outside the function, x:", x)


class StudentManager:
    def __init__(self):
        self.students_grades = {}
    # Method 1: Batch input of student names
    def add_students(self):
        while True:
            name = input("Enter student name (or type 'done' to finish): ")
            if name.lower() == 'done':
                break
            self.students_grades[name] = None  # Initial grade set to None
    # Method 2: Input grades for existing students
    def input_grades(self):
        if not self.students_grades:
            print("No students available. Please add students first.")
            return
        for student in self.students_grades:
            while True:
                try:
                    grade = float(input(f"Enter grade for {student}: "))
                    self.students_grades[student] = grade
                    break
                except ValueError:
                    print("Invalid input, please enter a number.")
    # Method 3: Output a student's grade based on their name
    def get_student_grade(self):
        name = input("Enter the name of the student to get the grade: ")
        if name in self.students_grades:
            grade = self.students_grades[name]
            if grade is not None:
                print(f"{name}'s grade is: {grade}")
            else:
                print(f"{name} does not have a grade yet.")
        else:
            print(f"No student found with the name {name}.")
    # Main menu to choose the operation
    def main_menu(self):
        while True:
            print("\nChoose an option:")
            print("1. Add students")
            print("2. Input grades")
            print("3. Get a student's grade")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_students()
            elif choice == '2':
                self.input_grades()
            elif choice == '3':
                self.get_student_grade()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
# Create an instance of the class and run the program
if __name__ == "__main__":
    manager = StudentManager()
    manager.main_menu()


class StudentManager:
    def __init__(self):
        self.students_grades = {}
    def add_students(self):
        while True:
            name = input("Enter student name (or 'done' to finish): ")
            if name.lower() == 'done':
                break
            self.students_grades[name] = None
    def input_grades(self):
        if not self.students_grades:
            print("No students available. Add students first.")
            return
        for student in self.students_grades:
            while True:
                try:
                    grade = float(input(f"Enter grade for {student}: "))
                    self.students_grades[student] = grade
                    break
                except ValueError:
                    print("Invalid input, enter a number.")
    def get_student_grade(self):
        name = input("Enter student's name: ")
        if name in self.students_grades:
            grade = self.students_grades[name]
            print(f"{name}'s grade: {grade}" if grade is not None else f"{name} has no grade.")
        else:
            print(f"No student found with the name {name}.")
    def main_menu(self):
        while True:
            choice = input("\n1. Add students\n2. Input grades\n3. Get grade\n4. Exit\nChoose: ")
            if choice == '1': self.add_students()
            elif choice == '2': self.input_grades()
            elif choice == '3': self.get_student_grade()
            elif choice == '4': break
if __name__ == "__main__":
    manager = StudentManager()
    manager.main_menu()
