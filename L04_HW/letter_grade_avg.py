from grade_compute import *

def containsDigit(s):
    for char in s:
        if char.isdigit():
            return True
    return False    

def processLine():
    while True:
        print("please enter 4 letter grades separated by a $ or 'q' to exit")
        raw_grades = input()
        raw_grades = raw_grades.upper()

        if raw_grades == 'Q':
            break
        elif raw_grades.count('$') != 3:
            continue
        elif raw_grades.count(' ') != 0:
            continue
        elif len(raw_grades) < 7 or len(raw_grades) > 11:
            continue
        elif containsDigit(raw_grades):
            continue
        else:
            break
    return raw_grades


def formatResults(letter_grades, lowest_letter, average_grade):
    print(" ---------------------------------------")
    print("|         GRADE REPORT SUMMARY          |")
    print("|---------------------------------------|")
    print(f"|Grades Entered:\t{letter_grades[0]}, {letter_grades[1]}, {letter_grades[2]}, {letter_grades[3]}\t|")
    print(f"|Lowest Grade Dropped:\t{lowest_letter}\t\t|")
    print(f"|Calculated Average:\t{round(average_grade, 2)}\t\t|")
    print(f"|Final Letter Grade:\t{numberToGrade(average_grade)}\t\t|")
    print(" ---------------------------------------")
    

def separateGrades(raw_grades):
    grades = []
    while True:
        if raw_grades.count('$') > 0:
            grade = raw_grades[0: raw_grades.index('$')]
            raw_grades = raw_grades[raw_grades.index('$') + 1: len(raw_grades)]
            grades.append(grade)
        else:
            grades.append(raw_grades)

            return grades

while True:
    raw_grades = processLine()

    if raw_grades == 'Q':
        break

    letter_grades = separateGrades(raw_grades)

    number_grades = gradeToNumber(letter_grades)

    number_grades.sort()

    lowest_grade = number_grades.pop(0)

    average_grade = 0
    for grade in number_grades:
        average_grade += grade

    average_grade /= 3.0

    lowest_letter = numberToGrade(lowest_grade)

    formatResults(letter_grades, lowest_letter, average_grade)