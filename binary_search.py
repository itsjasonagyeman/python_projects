space = []

number = int(input('Number between 1 and 100? '))
guess = 50
ask = input(f'Is your number {guess}? higher, lower or yes ')

if ask.lower() == 'higher': #number is higher than 50
    for i in range(50, 101):
        space.append(i)
    while True:
        guess = space[len(space)//2]
        ask = input(f'Is your number {guess}? higher, lower or yes ')
        if ask.lower() == 'yes':
            print(f'Your number is {guess}')
            break
        elif ask.lower() == 'higher':
            dupli = space
            space = []
            for i in range(guess, dupli[-1] + 1):
                space.append(i)
        elif ask.lower() == 'lower': 
            dupli = space
            space = []
            for i in range(dupli[0],guess + 1):
                space.append(i) 
            

if ask.lower() == 'lower': #number is lower than 50
    for i in range(1,51):
        space.append(i)
    while True:
        guess = space[len(space)//2]
        ask = input(f'Is your number {guess}? higher, lower or yes ')
        if ask.lower() == 'yes':
            print(f'Your number is {guess}')
            break
        elif ask.lower() == 'higher':
            dupli = space
            space = []
            for i in range(guess, dupli[-1] + 1):
                space.append(i)
        elif ask.lower() == 'lower': 
            dupli = space
            space = []
            for i in range(dupli[0],guess + 1):
                space.append(i) 