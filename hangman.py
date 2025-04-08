import random

words = ['python', 'java', 'javascript', 'kotlin', 'ruby', ' swift']

chosen_word = random.choice(words)
words_display = ['_' for _ in chosen_word]
attempts = 8

print('Welcome to Hangman')

while attempts > 0 and '_' in words_display:
    print('\n' + ''.join(words_display))
    guess = input('Guess? ').lower()
    if guess in words_display:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                words_display = guess
    else:
        print('Not in the word')
        attempts -= 1