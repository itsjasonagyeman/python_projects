grades = {}

def avg(first_value, second_value, third_value):
    ans = first_value + second_value + third_value 
    return ans/ 3

def grade_point(average):
    if average >= 90:
        return 'A'
    elif 79 < average < 90:
        return 'B'
    elif 69 < average < 80:
        return 'C'
    elif 59 < average < 70:
        return 'B'
    elif 49 < average < 60:
        return 'B'
    elif average < 50:
        return 'F'

while True:
    student_name = input('Type the students name ')
    first_grade = int(input('Type first grade '))
    second_grade = int(input('Type second grade '))
    third_grade = int(input('Type third grade '))
    average = avg(first_grade, second_grade, third_grade)
    gpa = grade_point(average)
    grades[student_name] = [first_grade, second_grade, third_grade, average, gpa]
    print(grades)
    end = input('Done? Yes or No ')
    if end.lower() == 'yes':
        break
    elif end.lower() == 'no':
        None
