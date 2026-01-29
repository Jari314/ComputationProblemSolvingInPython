import math

def gradeToNumber(letter_grades):
    number_grades = []

    for grade in letter_grades:
        num = 0

        if 'A' in grade:
            num = 3.67
        elif 'B' in grade:
            num = 2.67
        elif 'C' in grade:
            num = 1.67
        elif 'D' in grade:
            num = 0.67

        if '+' in grade:
            num += 0.33
        elif '-' in grade:
            num -= 0.34

        number_grades.append(num)
    return number_grades
            


def numberToGrade(num):
    if num > 3.0:
        grade = "A"
    elif num > 2.0:
        grade = "B"
    elif num > 1.0:
        grade = "C"
    elif num > 0.0:
        grade = "D"
    else:
        grade = "F"

    if num - math.floor(num) >= 0.0 and num - math.floor(num) < 0.33:
        grade += "+"
    elif num - math.floor(num) >= 0.33 and num - math.floor(num) < 0.67:
        grade += "-"

    return grade