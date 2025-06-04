from db import connect

def host():
    while True:
        print("\n--- Host Menu ---")
        print("1. Add Question")
        print("2. Update Question")
        print("3. Delete Question")
        print("4. View Questions")
        print("5. Logout")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_question()
        elif choice == 2:
            update_question()
        elif choice == 3:
            delete_question()
        elif choice == 4:
            view_questions()
        elif choice == 5:
            print("Logging out...")
            break
        else:
            print("Invalid choice.")

def add_question():
    conn = connect()
    cursor = conn.cursor()
    qid = int(input("Enter question ID: "))
    qtext = input("Enter question text: ")
    correct_option = input("Enter correct option: ")
    score = 1
    cursor.execute("INSERT INTO questions(question_id, question_text, correct_option, score) VALUES(%s, %s, %s, %s)", (qid, qtext, correct_option, score))
    conn.commit()
    print("Question added.")
    conn.close()

def update_question():
    conn = connect()
    cursor = conn.cursor()
    qid = int(input("Enter question ID to update: "))
    new_text = input("Enter new question: ")
    new_option = input("Enter new correct option: ")
    cursor.execute("UPDATE questions SET question_text=%s, correct_option=%s WHERE question_id=%s", (new_text, new_option, qid))
    conn.commit()
    print("Question updated.")
    conn.close()

def delete_question():
    conn = connect()
    cursor = conn.cursor()
    qid = int(input("Enter question ID to delete: "))
    cursor.execute("DELETE FROM questions WHERE question_id=%s", (qid,))
    conn.commit()
    print("Question deleted.")
    conn.close()

def view_questions():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions")
    for row in cursor.fetchall():
        print(row)
    conn.close()

# def view_student_scores():
#     conn = connect()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM marks")
#     for row in cursor.fetchall():
#         print(row)
#     conn.close()

if __name__=="__main__":
    host()