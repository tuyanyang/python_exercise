def computeGrade(score):
    if score < 0 or score > 1:
        grade = 'Bad score'
    elif score > 0.9:
        grade = 'A'
    elif score > 0.8:
        grade = 'B'
    elif score > 0.7:
        grade = 'C'
    elif score > 0.6:
        grade = 'D'
    else:
        grade = 'F'
    return grade


scoreStr=input('Enter score: ')
try:
    score = float(scoreStr)
    grade = computeGrade(score)
    print(grade)
except ValueError:
    print('Bad score')

