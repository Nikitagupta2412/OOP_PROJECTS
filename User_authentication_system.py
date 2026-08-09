# Building the project from scratch 
users=[]
class user:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.__password = password

    def check_password(self,input_password):
        if input_password == self.__password:
            return True
        else:
            return False
        
def signup():
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    new_user = user(username,email,password)
    users.append(new_user)
    print("User signed up successfully!")

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    for user in users:
        if user.email == email and user.check_password(password):
            print("Login successful!")
            return
    print("Invalid email or password.")
    
while True:
    choice = input("Enter 'signup' to sign up, 'login' to log in, or 'exit' to quit: ")
    if choice == 'signup':
        signup()
    elif choice == 'login':
        login()
    elif choice == 'exit':
        break
    else:
        print("Invalid choice. Please try again.")
    
