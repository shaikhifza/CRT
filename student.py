from db import connect
def student_menu(username):
    while True:
        print(f"---Welcome to the Mania, {username}---")
        print("1.Take Quiz")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            take_quiz(username)
        else:
            print("Invalid choice. Please try again...")

def take_quiz(username):
    conn = connect()
    cursor = conn.cursor()
    query=("SELECT question_id, question_text, correct_option FROM questions")
    cursor.execute(query)
    questions = cursor.fetchall()
    score = 0
    for q in questions:
        question_id, question_text, correct_option = q
        print("Question:")
        print(question_text)
        value = input("Enter your answer: ")
        if value== correct_option:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. Correct answer was: {correct_option}\n")
    result = f"{score}/{len(questions)}"
    print(f"Your final score is: {result}")
    conn.close()

if __name__=="__main__":
    user_name=input("Enter your username: ")
    student_menu(user_name)