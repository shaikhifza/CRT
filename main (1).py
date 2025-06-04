from auth import login, signup
from host import host
from student import student_menu

def main():
    while True:
        print("\n--- Online Quiz System ---")
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")
        ch = input("Enter your choice: ")
        if ch == '1':
            user_id=input("Enter user id: ")
            user_name=input("Enter user name: ")
            password=input("Enter password: ")
            role=input("Enter Role(host/student): ")
            signup(user_id,user_name,password,role)
        elif ch == '2':
            user_id=input("Enter user id: ")
            user_name=input("Enter user name: ")
            password=input("Enter password: ")
            role=input("Enter Role(host/student): ")
            login(user_id,user_name,password,role)
        elif ch == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()