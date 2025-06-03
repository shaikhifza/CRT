from db import connect
connection=connect()
if connection:
    print("connection established successfully")
else:
    print("connection failed")
def insert_data():
    
    roll_no=int(input("Enter roll number: "))
    name=input("enter name: ")
    branch=input("enter branch: ")
    cursor=connection.cursor()
    query="insert into student(roll_no,name,branch)values(%s,%s,%s)"
    values=(roll_no,name,branch)
    cursor.execute(query,values)
    connection.commit()
    print("Data inserted successfully")
def fetch_data():
    cursor=connection.cursor()
    query="select*from student "
    cursor.execute(query)
    results=cursor.fetchall()
    for row in results:
        print(row)
def update_data():
    roll_no=int(input("Enter roll number: "))
    name=input("enter name: ")
    branch=input("enter branch: ")
    cursor=connection.cursor()
    query="update student set name=%s,branch=%s where roll_no=%s"
    values=(name,branch,roll_no)
    cursor.execute(query,values)
    connection.commit()
    print("Data updated successfully")
while True:
    print("\n---welcome to the student database--")
    print("1.Insert Data")
    print("2.Fetch Data")
    print("3.update Data")
    print("4.Exit")
    choice=int(input("Enter the choice:"))
    if choice==1:
        insert_data()
    elif choice==2:
        fetch_data()
    elif choice==3:
        update_data()
    elif choice==4:
        print("Exit..")
        break
 
