"""
Quiz console application, which counts percentage of right answers
"""


def quiz():
    questions = {
        'question1': {
            'question': 'What is the capital of Great Britain?',
            'answer': 'London'
        },
        'question2': {
            'question': 'Who was the first man in the space?',
            'answer': 'Yuri Gagarin'
        },
        'question3': {
            'question': 'What is the longest river in Africa?',
            'answer': 'the Nile'
        },
        'question4': {
            'question': 'How many presidents were elected in the USA from 2000 till 2022?',
            'answer':'5 five'
        },
        'question5': {
            'question': 'What is the smallest continent in the Earth?',
            'answer': 'Australia'
        }
    }

    score = 0

    for question, value in questions.items():
        print(value['question'])
        answer = input('Your answer?\n')
        print('-' * 60)
        if answer.lower() == value['answer'].lower() or answer.lower() in value['answer'].lower().split():
            score += 1
            print('Correct!')
            print('-' * 60)
            print()
        else:
            print('Wrong!')
            print('-' * 60)
            print()

    print(f'Your score is {score}! The percentage of right answers is {int(score / 5 * 100)}%')

