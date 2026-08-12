# Building the project from scratch

import json
import os


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def check_password(self, input_password):
        if input_password == self.__password:
            return True
        else:
            return False

    def change_password(self, new_password):
        self.__password = new_password

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.__password
        }


# Store all User objects here
users = []


# Load existing users from JSON
if os.path.exists("users.json"):
    with open("users.json", "r") as file:
        data = json.load(file)

    for item in data:
        new_user = User(
            item["username"],
            item["email"],
            item["password"]
        )
        users.append(new_user)


def save_users():
    data = []

    for user in users:
        data.append(user.to_dict())

    with open("users.json", "w") as file:
        json.dump(data, file, indent=4)


def signup():
    username = input("Enter your username: ")
    email = input("Enter your email: ")

    for user in users:
        if user.email == email:
            print("Email already exists. Please use a new email.")
            return

    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")

    if password != confirm_password:
        print("Passwords do not match!")
        return

    if len(password) < 8:
        print("Password must be at least 8 characters long!")
        return

    new_user = User(username, email, password)
    users.append(new_user)

    save_users()

    print("User signed up successfully!")


def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for user in users:
        if user.email == email and user.check_password(password):
            print("Login successful!")
            return user

    print("Invalid email or password.")
    return None


def dashboard(user):
    while True:
        print("\nWelcome back,", user.username)
        print("1. View Profile")
        print("2. Change Password")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Username:", user.username)
            print("Email:", user.email)

        elif choice == "2":
            current_password = input("Enter your current password: ")

            if user.check_password(current_password):
                new_password = input("Enter your new password: ")
                confirm_password = input("Confirm your new password: ")

                if new_password != confirm_password:
                    print("Passwords do not match!")
                    continue

                if len(new_password) < 8:
                    print("Password must be at least 8 characters long!")
                    continue

                user.change_password(new_password)

                # Save the changed password to JSON
                save_users()

                print("Password changed successfully!")

            else:
                print("Incorrect current password!")

        elif choice == "3":
            print("Logged out successfully!")
            break

        else:
            print("Invalid choice. Please try again.")


# Main menu
logged_in_user = None

while True:
    choice = input(
        "\nEnter 'signup' to sign up, "
        "'login' to log in, or "
        "'exit' to quit: "
    )

    if choice == "signup":
        signup()

    elif choice == "login":
        logged_in_user = login()

        if logged_in_user is not None:
            dashboard(logged_in_user)
            logged_in_user = None

    elif choice == "exit":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")