import mysql.connector

def connect():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="#S@i09_16", 
        database="online_quiz_system"
    )
    return conn
if(connect()):
    print("Connection established successfully")
else:
    print("Connection failed")