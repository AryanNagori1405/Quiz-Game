Purpose:
The code defines a simple quiz game where the user answers multiple-choice questions and receives a score based on their answers.

Breakdown:
Questions List:
A list of dictionaries, where each dictionary represents a question with its options and the correct answer.

questions = [
    {
        'question' : 'Which of the following is a mutable data type in Python?',
        'options' : ['a) List', 'b) Tuple', 'c) String', 'd) Integer'],
        'actual_answer' : 'a'
    },
    ...
]
QuizGame Function:

A function QuizGame(questions) that takes the list of questions as input and runs the quiz game.

def QuizGame(questions):
    score = 0  # Initialize score to 0
    ...
Iterating Through Questions:

A for-loop iterates over the list of questions. enumerate(questions, start=1) is used to get both the index and the question, starting the index at 1.

for i, ques in enumerate(questions, start=1):
    print(f"{i}.{ques['question']}")  # Print the question number and text
    ...
Displaying Options:

A nested loop prints each option for the current question.

for option in ques['options']:
    print(option)
User Input:

The user is prompted to enter their answer, which is converted to lowercase for consistency.

user_input = input("Enter the answer (a, b, c or d): ").lower()
Checking the Answer:

The user's answer is compared to the correct answer (ques['actual_answer']).

If the answer is correct, the score is incremented, and a congratulatory message is printed.

If the answer is incorrect, the correct answer is shown.

if user_input == ques['actual_answer']:
    print("Correct, Hooray!!!")
    score += 1
else:
    print(f"Wrong answer, The correct answer was {ques['actual_answer']}")
Displaying the Score:

After each question, the current score is displayed.

print(f"Your score is {score}\n")
Running the Game:

The QuizGame(questions) function is called to start the game.

QuizGame(questions)
Summary:
The code creates an interactive quiz game where the user answers multiple-choice questions.

The user's score is updated based on their answers, and feedback is provided after each question.

The game runs until all questions have been answered, showing the user's score after each question.
