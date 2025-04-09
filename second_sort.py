numbers = []

for i in range (1,6):
    number = int(input('Write a number '))
    numbers.append(number)

print(numbers)
    
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j:
            if numbers[i] < numbers[j]:
                print(f'{numbers[i]} is less than {numbers[j]}')
                print(f'So swap {numbers[i]} and {numbers[j]}')
                numbers[i], numbers[j] = numbers[j], numbers[i]
                print(numbers)


