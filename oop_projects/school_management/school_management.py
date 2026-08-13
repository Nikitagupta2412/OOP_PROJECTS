import json 
import os
from abc import ABC,abstractmethod
from pathlib import Path

database = "School_data.json"
data = {"students" : [] , "teachers" : []}

if Path(database).exists():
    with open (database , "r") as f:
        content = f.read()
        if content :
            data = json.loads(content)

def save():
    with open (database,"w") as f:
        json.dump(data,f,indent=4)

class person(ABC):

    @abstractmethod
    def register():
        pass

    @abstractmethod
    def show_details():
        pass

    @abstractmethod
    def get_roles():
        pass

    @staticmethod
    def validate_email(email):
        if "@" in email and "." in email:
            return True
        else:
            return False

class students(person):

    def register(self):
        name = input("enter name : ")
        roll_no = int(input("enter roll no : "))
        email = input("enter email: ")
        standard = input("enter standard : ")
        age = int(input("enter your age: "))

        if not person.validate_email(email):
            print ("invalid email")
            return

        for i in data["students"]:
            if i["roll_no"] == roll_no:
                print("rollno already exists")
                return

        data["students"].append({

            "name" : name,
            "roll_no" : roll_no,
            "email" : email,
            "standard" : standard,
            "grades" : {}

        })
        save()
        print("student registerred successfullyy")

    def get_roles(self):
        return "student"
    
    def show_details(self):
        roll_no = int (input("enter the roll no: "))
        for i in data["students"]:
            if i["roll_no"]== roll_no:
                print(i,"the students details are printed")
        print("student nott foundd")

    def grade(self):
        roll_no = int (input("enter the roll no of the student: "))
        subject = input("enter the subjects: ")
        marks = float(input(" enter the grades: "))

        for i in data["students"]:
            if i ["roll_no"] == roll_no:
                i['grades'][subject] = marks
                save()
                print("Grades added successfully")
                return
        print("student nnot found")

class teachers(person):

   def register(self):
        name = input("enter name : ")
        emp_no = int(input("enter emp no : "))
        email = input("enter email : ")
        post = input("enter pgt or tgt along woth subject ")
        age = int(input("enter your age : "))

        if not person.validate_email(email):
            print ("invalid email")
            return

        for i in data["students"]:
            if i["emp_no"] == emp_no:
                print("rollno already exists")
                return

        data["teachers"].append({
            "name" : name,
            "empno" : emp_no,
            "email" : email,
            "post" : post,
        })
        save()
        print(f"information saved for student{name}")

   def get_roles(self):
       return "Teacher"

   def show_details(self):
    
    emp_no = int (input("enter the emp no : "))
    
    for i in data["teachers"]:
        if i["emp_no"] == emp_no:
                print(i,"the teacherss details are printed")

stud = students()
teach = teachers()

while True:

    print("enter 1 to register a student")
    print("enter 2 to register a teacher")
    print("enter 3 to enter grades")
    print("enter 4 to look at the details of student")
    print("enter 5 to look at the detials of a teacher")
    print("enter 6 to look at the current data")
    print("enter 7 to exit the program")

    choice = (input("enter your choice : "))
    if choice == "1":
        stud.register()
    elif choice == "2":
        teach.register()
    elif choice == "3":
        stud.grade()
    elif choice == "4":
        stud.show_details()
    elif choice == "5":
        teach.show_details()
    elif choice == "6":
        print(data)
    elif choice == "7":
        break
    