# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 18:02:34 2026

@author: amna-
"""
# Student Grade Manager
# A simple console program to track students and their scores

def show_menu(): # Defines a function, a named reusable block of code ready to be called later
    # Displays the list of options to the user
    print("\n--- Student Grade Manager ---")
    print("1. Add a student")
    print("2. View all students")
    print("3. Exit")
    
# Main program loop
running = True

while running:
    show_menu() # A function call, runs whatevers inside show_menu
    choice = input("Choose an option (1-3):")
    
    if choice == "1":
        print("Add student - coming soon")
    elif choice == "2":
        print("View students - coming soon")
    elif choice == "3":
        print("Goodbye!")
        running = False
    else:
        print("Invalid choice, please try again")
    
