# These are the set of questions and options displayed in front of the user
questions = [
    {
        'question' : 'Which of the following is a mutable data type in Python?',
        'options' : ['a) List', 'b) Tuple', 'c) String', 'd) Integer'],
        'actual_answer' : 'a'
    },
    {
        'question' : 'What does the len() function do in Python?',
        'options' :
            [
                'a) Calculates the sum of all elements in a list',
                'b) Returns the number of items in an object',
                'c) Finds the maximum value in a list',
                'd) Sorts a list in ascending order'
            ],
        'actual_answer' : 'b'
    },
    {
        'question' : 'Which of the following is a Python built-in function used to create an iterator from an iterable?',
        'options' : ['a) iter()', 'b) next()', 'c) map()', 'd) filter()'],
        'actual_answer' : 'a'
    },
    {
        'question' : 'In Python, which keyword is used to handle exceptions?',
        'options' : ['a) try', 'b) catch', 'c) except', 'd) finally'],
        'actual_answer' : 'c'
    },
    {
        'question' : 'What will be the output of the following code?\nx = [1, 2, 3]\nprint(x[1:3]',
        'options' : ['a) [1, 2, 3]', 'b) [1, 2]', 'c) [2, 3]', 'd) [1, 3]'],
        'actual_answer' : 'c'
    }
]

def QuizGame(questions):
    print("Welcome to Quiz Game")
    score = 0    # Here score is initialized to zero so later it can be incremented
    for i, ques in enumerate(questions, start=1):    # This 'for' loop will display the question 
        print(f"{i}.{ques['question']}")
        for option in ques['options']:     # This 'for' loop will display the options for that question 
            print(option)
        user_input = input("Enter the answer (a, b, c or d): ").lower()
        if user_input == ques['actual_answer']:    # This 'if' will check whether the input given by user is same as the actual answer
            print("Correct, Hooray!!!")    # If Yes, then this will be printed
            score += 1    # And the score will be incremented by 1
        else:
            print(f"Wrong answer, The correct answer was {ques['actual_answer']}")    # If No, then this will be printed
        print(f"Your score is {score}\n")    # At last the total score will be printed

QuizGame(questions)
