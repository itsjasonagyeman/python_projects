sentence = input('type a sentence > ')

word_count = len(sentence.split())
letter_count = sum(1 for char in sentence if char.isalpha())

print(f'The number of words are {word_count}')
print(f'The number of letters are {letter_count}')