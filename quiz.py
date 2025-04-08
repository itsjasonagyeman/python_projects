questions = [
    {
        'prompt': 'What is the capital of France?',
        'options': ['A. Paris', 'B. London', 'C. Berlin', 'D. Madrid'],
        'answer': 'A',
    },
    {
        'prompt': 'Which language is primarily spoken in Brazil',
        'options': ['A. Spanish', 'B. Portuguese', 'C. English', 'D.French'],
        'answer': 'B',
    },
    {
        'prompt': 'What is the smallest prime number?',
        'options': ['A. 1', 'B. 2', 'C. 3', 'D. 5'],
        'answer': 'B',
    },
    {
        'prompt': "Who wrote 'To Kill a MockingBird?'",
        'options': ['A. Harper Lee', 'B. Mark Twain', 'C. J.K. Rowling', 'D. Ernest Hemmingway'],
        'answer': 'A',
    },
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question['prompt'])
        for option in question['options']:
            print(option)
        prompt = str(input('> '))
        if prompt.upper == question['answer']:
            score += 1
    print(f'Your score is {score}')


run_quiz(questions)