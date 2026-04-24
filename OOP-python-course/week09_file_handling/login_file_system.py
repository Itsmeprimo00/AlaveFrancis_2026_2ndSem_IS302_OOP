def register_FGA():
    username_FGA = input("Enter username: ")
    password_FGA = input("Enter password: ")
    with open("users.txt", "a") as file_FGA:
        file_FGA.write(username_FGA + "," + password_FGA + "\n")
    print("Registration successful!")

def login_FGA():
    username_FGA = input("Enter username: ")
    password_FGA = input("Enter password: ")
    try:
        with open("users.txt", "r") as file_FGA:
            for line_FGA in file_FGA:
                stored_user_FGA, stored_pass_FGA = line_FGA.strip().split(",")
                if username_FGA == stored_user_FGA and password_FGA == stored_pass_FGA:
                    print("Login successful!")
                    return
        print("Invalid credentials!")
    except FileNotFoundError:
        print("No users registered yet!")

def main_FGA():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice_FGA = input("Enter choice: ")
        
        if choice_FGA == "1":
            register_FGA()
        elif choice_FGA == "2":
            login_FGA()
        elif choice_FGA == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main_FGA()

