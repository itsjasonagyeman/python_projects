import random

number = random.randint(1, 9)
guess = int(input('Guess the number? '))

attempts = 5

while attempts > 0 and guess != number:
    print('Wrong, try again')
    attempts -= 1
    print(f'Attempts left {str(attempts)}')
    guess = int(input('Guess the number? '))

if number == guess:
    print('You Won!')
elif attempts == 0:
    print('You run out of attempts')
    print(f'The number was {number}')

    
        