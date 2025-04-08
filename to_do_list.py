todo = []

while True:
    actions = input(
'''
1 for Add to list
2 for Remove from list
3 for Clear list
Any other number to View list
e to end

'''
    )
    if actions == '1':
        task = input('task > ')
        todo.append(task)
        print(todo)
    elif actions == '2':
        print(todo)
        task = int(input('Which index should be removed? '))
        todo.pop(task)
        print(todo)
    elif actions == '3':
        todo.clear()
        print('List cleared')
        print(todo)
    elif actions.lower() == 'e':
        print('ended')
        break
    else:
        print(todo)