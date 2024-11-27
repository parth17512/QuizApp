import tkinter as tk
from tkinter import messagebox

# Function to open quiz window.
def open_quiz_window():
    # Create a new window for the quiz.
    quiz_window = tk.Tk()
    quiz_window.title("Quiz Application")
    quiz_window.geometry("900x600")  # Set a more reasonable size for the window.
    quiz_window.resizable(False, False)  # Disable resizing for a cleaner look.

    # Set a professional background color.
    quiz_window.config(bg="#f4f4f4")  # Light gray for a clean and neutral background.

    # Sample questions and answers.
    questions = [
        {"question": "Which of the following is the correct syntax to create a function in Python?", "options": ["create function():", "function def():", "def function():", "function create():"], "answer": "def function():"},
        {"question": "Which method can be used to add an element to the end of a list in Python?", "options": ["add()", "append()", "insert()", "extend()"], "answer": "append()"},
        {"question": "Which of the following is used to define a block of code in Python?", "options": ["Parentheses()", "Indentation (spaces or tabs)", "Curly braces {}", "Square brackets []"], "answer": "Indentation (spaces or tabs)"},
        {"question": "What does the len() function do?", "options": ["Returns the number of characters in a string", "Returns the length of a list, tuple, or string", "Returns the sum of the elements in a list", "Returns the last element of a list"], "answer": "Returns the length of a list, tuple, or string"},
        {"question": "Which of the following is a valid way to comment a single line in Python?", "options": ["/* This is a comment */", "# This is a comment", "// This is a comment", "<!-- This is a comment -->"], "answer": "# This is a comment"},
        {"question": "Which operator is used to compare two values in Python?", "options": ["=", "==", ":=", "!="], "answer": "=="},
        {"question": "Which of the following methods can be used to remove an item from a list in Python?", "options": ["remove()", "delete()", "pop()", "Both a and c"], "answer": "Both a and c"},
    ]

    score = 0  # Initialize the score.
    current_question_index = 0  # Track the current question.

    # Function to check the selected answer.
    def check_answer(selected_answer, correct_answer):
        nonlocal score
        if selected_answer == correct_answer:
            score += 1
        next_question()

    # Function to show the next question.
    def next_question():
        nonlocal current_question_index
        if current_question_index < len(questions):
            question_data = questions[current_question_index]
            question_label.config(text=f"Q{current_question_index + 1}: {question_data['question']}")

            # Update options.
            for i, option in enumerate(question_data["options"]):
                option_buttons[i].config(
                    text=option,
                    command=lambda option=option: check_answer(option, question_data["answer"])
                )

            current_question_index += 1
        else:
            # Show the final score and close the quiz window.
            messagebox.showinfo("Quiz Finished", f"Your score is: {score}/{len(questions)}")
            quiz_window.quit()

    # Create a label for the question with a professional style.
    question_label = tk.Label(
        quiz_window, 
        text="", 
        font=("Helvetica", 16, "bold"), 
        width=70, 
        wraplength=800, 
        bg="#f4f4f4", 
        fg="#333333"  # Dark gray for text color.
    )
    question_label.pack(pady=20)

    # Create buttons for answer options with a professional look.
    option_buttons = []
    for _ in range(4):
        button = tk.Button(
            quiz_window,
            font=("Helvetica", 12),
            width=40,
            height=2,
            bg="#e0e0e0",  # Light gray background for buttons.
            fg="#000000",  # Black text for buttons.
            activebackground="#d6d6d6",  # Slightly darker gray when hovered.
            activeforeground="#000000",  # Black text when hovered.
            relief="groove",  # Professional button relief style.
        )
        button.pack(pady=10)
        option_buttons.append(button)

    # Start the quiz with the first question.
    next_question()

    # Start the Tkinter event loop for the quiz window.
    quiz_window.mainloop()

# Directly open the quiz window when the application starts.
open_quiz_window()
