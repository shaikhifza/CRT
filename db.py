import mysql.connector
def connect():
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="HIFZA@SHAIK18/",
        database="practice_crt"
    )
    return connection
if(connect()):
    print("connection established")
else:
    print("connection failed")

