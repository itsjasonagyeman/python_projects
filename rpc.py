import random
import time

while True:
    cpu = ['rock', 'paper', 'scissors']
    cpu_choice = random.choice(cpu)
    time.sleep(0.5)
    play = input(
'''
Play

1 for Rock,
2 for Paper,
3 for Scissors
4 for exit

'''
    )
    if play == '1' and cpu_choice == 'rock' or play =='2' and cpu_choice == 'paper' or play == '3' and cpu_choice == 'scissors':
        print('draw')
    elif play == '1' and cpu_choice == 'scissors' or play == '2' and cpu_choice == 'rock' or play == '3' and cpu_choice == 'paper':
        print('you win')
    elif play == '4':
        print('exit')
        break
    else:
        print('you lose')




