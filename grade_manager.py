# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 18:02:34 2026

@author: amna-
"""
# Student Grade Manager
# A simple console program to track students and their scores

# list for holding all students
# Each student stored as a dictionary: {"name": ..., "score", ...}

students = [] # an empty list, container that can hold multiple items

def show_menu(): # Defines a function, a named reusable block of code ready to be called later
    # Displays the list of options to the user
    print("\n--- Student Grade Manager ---")
    print("1. Add a student")
    print("2. View all students")
    print("3. Show class average")
    print("4. Exit")
    
def add_student():
    # Asks user for name and score, then stores it in students list
    name = input("Enter student name:")
    score = float(input("Enter student score:"))
    
    # Dictionary groups related data together under labeled "keys"
    # Stores labeled data
    student = {"name": name, "score": score}
    students.append(student) # append() adds this student to the end of the list
    
    print(name, "has been added.")

def view_students():
    # Prints every student currectly stored in the list
    if len(students) == 0:
        print("No students added yet.")
    else:
        for student in students:
            if student["score"] >= 50:
                status = "Pass"
            else:
                status = "Fail"
            print(student["name"], "-", student["score"], status)

def show_average(): # Calculates the average score 
    if len(students) == 0:
        print("No students to average")
    else:
        total = 0
        for student in students:
            total = total + student["score"]
        average = total / len(students)
        print("Class average:", round(average,2))
            
# Main program loop
running = True

while running:
    show_menu() # A function call, runs whatevers inside show_menu
    choice = input("Choose an option (1-3):")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        show_average()
    elif  choice == "4":
        print("Goodbye!")
        running = False
    else:
        print("Invalid choice, please try again")
    
