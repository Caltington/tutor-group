#Imports
import random
#Login
def login():
    inputusername = input("Enter your username: ")
    if inputusername == "admin":
        print("Admin Bypass")
        print("Welcome", inputusername + "!\n")
        menu()
    inputpassword = input("Enter your password: ")
    username = ["Leemaster67", "Gerald43", "Steve49"]
    password = ["TheRealLeemaster67!", "Greatgerald4", "Stevethethird"]
    for x in username:
        if x == inputusername:
            position = username.index(x)
            if inputpassword == password[position]:
                print("Valid login")
                print("Welcome", inputusername + "!\n")
                menu()
    print("Invalid username or password")
    login()
def Add_Student():
    student_ID = random.randint(1000,9999)
    firstname = input("Enter the student's first name: ")
    secondname = input("Enter the student's second name: ")
    dateofbirth = input("Enter student's date of birth: ")
    address = input("Enter student's address: ")
    phonenumber = input("Enter the student's phone number: ")
    gender = input("Enter the student's gender: ")
    tutorgroup = input("Enter the student's tutor group: ")
    with open("StudentDatabase.csv", "a") as file:
        file.write(str(student_ID) + "," + firstname + "," + secondname + "," + dateofbirth + "," + address + "," + phonenumber + "," + gender + "," + tutorgroup + ",\n")
    print("Added to database")
    menu()
#Student Search
def Search_Student():
    counter = 0
    student = input("Enter the student ID: ")
    with open("StudentDatabase.csv", "r") as file:
        line = file.readline()
        while(line):
            data=line.split(",")
            if data[0] == student:
                print("The student with the ID", student, "is named", data[1], data[2], "and their gender is", data[6] + ".\n" + "The student's date of birth is", data[3], "and their tutor group is", data[7] + "\n" + "The student's address is " + data[4] + ".\n" + "Their phone number is", data[5] + "\n")
                counter = 1
            line = file.readline()
        if counter == 0:
            print("No data was associated with the ID of", student)
    menu()
#Generate report
def Generate_Report():
    counter = 0
    student = input("Enter the student's ID: ")
    with open("StudentDatabase.csv", "r") as file:
        line = file.readline()
        while(line):
            data=line.split(",")
            if data[0] == student:
                names = "Name: " + data[1] + " "+  data[2] + "\n"
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
#Menu
def menu():
    print("Tutor Group Program")
    print("Do you wish to add a student, search for a student, generate a report or log out?")
    choice = input("1. Add student\n2. Search for student\n3. Generate report\n4. Log out\n")
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
login()
