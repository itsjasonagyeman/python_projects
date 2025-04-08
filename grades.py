while True:
    grades = {}
    student_name = input('Type the students name ')
    first_grade = input('Type first grade ')
    second_grade = input('Type first grade ')
    third_grade = input('Type first grade ')
    grades[student_name] = {first_grade, second_grade, third_grade}
    for name, info in grades.items():
        print(f'{name}: {info}')
    end = input('Done? Yes or No ')
    if end.lower() == 'yes':
        break
    elif end.lower() == 'no':
        None
