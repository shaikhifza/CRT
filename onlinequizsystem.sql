CREATE DATABASE online_quiz_system;
USE online_quiz_system;

CREATE TABLE users_table (
    user_id VARCHAR(20) PRIMARY KEY,
    user_name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100),
    role VARCHAR(50)
);

CREATE TABLE questions (
    question_id INT PRIMARY KEY,
    question_text TEXT,
    correct_option VARCHAR(10),
    score INT
);

CREATE TABLE marks (
    user_id VARCHAR(20),
    total_score INT,
    FOREIGN KEY (user_id) REFERENCES users_table(user_id)
);