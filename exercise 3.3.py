while True:
    scoreStr = input("Input score between 0.0 and 1.0:")
    try:
        score = float(scoreStr)
    except ValueError:
        print("Bad score")
        #continue

    if score < 0.0 or score > 1.0:
        print("Bad score")
        continue

    if score >= 0.9 and score <= 1.0:
        grade = "A"
    elif score >= 0.8 and score <= 1.0:
        grade = "C"
    elif score >= 0.7 and score <= 1.0:
        grade = "D"
    elif score >= 0.6 and score <= 1.0:
        grade = "E"
    elif score >= 0.0 and score <= 1.0:
        grade = "F"
    else:
        grade ="Unknown"
    print(grade)
