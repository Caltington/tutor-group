import tkinter as tk
from tkinter import simpledialog

import random


def login():
    input_username = simpledialog.askstring("Input", "Enter your username:")
    if input_username == "admin":
        print("Admin Bypass")
        print("Welcome", input_username + "!\n")
        menu()
    input_password = simpledialog.askstring("Input", "Enter your password:")
    username = "Leemaster67"
    password = "TheRealLeemaster67!"
    if input_username == username:
        if input_password == password:
            print("Valid login")
            print("Welcome", username + "!\n")
            menu()
        else:
            print("Invalid password")
            login()
    else:
        print("Username not found!")
        login()


def Add_Student():
    student_ID = random.randint(1000, 9999)
    firstname = simpledialog.askstring("Input", "Enter the student's first name:")
    secondname = simpledialog.askstring("Input", "Enter the student's second name:")
    dateofbirth = simpledialog.askstring("Input", "Enter student's date of birth:")
    address = simpledialog.askstring("Input", "Enter student's address:")
    phonenumber = simpledialog.askstring("Input", "Enter the student's phone number:")
    gender = simpledialog.askstring("Input", "Enter the student's gender:")
    tutorgroup = simpledialog.askstring("Input", "Enter the student's tutor group:")

    with open("StudentDatabase.csv", "a") as file:
        file.write(
            f"{str(student_ID)},{firstname},{secondname},{dateofbirth},{address},{phonenumber},{gender},{tutorgroup},\n"
        )
    print("Added to database")
    menu()


def Search_Student():
    counter = 0
    student = simpledialog.askstring("Input", "Enter the student ID:")
    with open("StudentDatabase.csv", "r") as file:
        line = file.readline()
        while line:
            data = line.split(",")
            if data[0] == student:
                print(
                    "The student with the ID",
                    student,
                    "is named",
                    data[1],
                    data[2],
                    "and their gender is",
                    data[6] + ".\n"
                    + "The student's date of birth is",
                    data[3],
                    "and their tutor group is",
                    data[7]
                    + "\n"
                    + "The student's address is "
                    + data[4]
                    + ".\n"
                    + "Their phone number is",
                    data[5] + "\n",
                )
                counter = 1
            line = file.readline()
        if counter == 0:
            print("No data was associated with the ID of", student)
    menu()


def Generate_Report():
    counter = 0
    student = simpledialog.askstring("Input", "Enter the student's ID:")
    with open("StudentDatabase.csv", "r") as file:
        line = file.readline()
        while line:
            data = line.split(",")
            if data[0] == student:
                names = "Name: " + data[1] + " " + data[2] + "\n"
                gender = "Gender: " + data[6] + "\n"
                grades = "Grades: BAD\n"
                counter = 1
            line = file.readline()
        if counter == 0:
            print("No data was associated with the ID of", student)
        elif counter == 1:
            with open(student + "report.txt", "w") as file:
                file.write(names + gender + grades)
                print("Report card generated as", student + "report.txt")
    menu()


def menu():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    choice = simpledialog.askstring("Menu", "1. Add student\n2. Search for student\n3. Generate report\n4. Log out\n")

    if choice == "1":
        Add_Student()
    elif choice == "2":
        Search_Student()
    elif choice == "3":
        Generate_Report()
    elif choice == "4":
        print("Logging out...")
        exit()
    else:
        print("Invalid choice!")
        print("Only enter 1, 2, 3 or 4!")
        menu()


if __name__ == "__main__":
    login()