while True:
    number = int(input('Write an even or odd number  or type exit > '))
    if number % 2 == 0:
        print('This number is even')
    elif number == 1:
        break
    else:
        print('This number is odd')