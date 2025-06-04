from db import connect

def signup(user_id,user_name, password, role):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users_table WHERE user_name = %s", (user_name,))
    if cursor.fetchone():
        print("Username already exists.")
    else:
        cursor.execute("INSERT INTO users_table(user_id,user_name, password, role) VALUES(%s, %s, %s,%s)",
                       (user_id,user_name, password, role))
        conn.commit()
        print("Signup successful.")
    cursor.close()
    conn.close()

def login(user_id,user_name, password, role):
    conn = connect()
    cursor = conn.cursor()
    if role == "host":
        if user_name == "host" and password == "host123":
            print("Host login successful.")
        else:
            print("Invalid host credentials.")
    elif role == "student":
        cursor.execute("SELECT * FROM users_table WHERE user_name=%s AND password=%s", (user_name, password))
        if cursor.fetchone():
            print(f"Welcome {user_name}")
        else:
            print("Invalid student credentials.")
    else:
        print("Invalid role.")
    cursor.close()
    conn.close()
    
if __name__ == "__main__":
    query= input("Do you want to login or signup? ").strip().lower()
    role = input("Enter role (host/student): ").strip().lower()
    user_id=int(input("Enter the user_id: "))
    user_name = input("Enter username: ")
    password = input("Enter password: ")

    if query == "signup":
        signup(user_id,user_name, password, role)
    elif query == "login":
        login(user_id,user_name, password, role)
    else:
        print("Invalid action.")