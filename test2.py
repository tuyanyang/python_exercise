while True:
    scoreStr = input("Input score between 0.0 and 1.0:")
    try:
        score = float(scoreStr)
    except:
        print("Bad format")
        continue

    if score < 0 or score > 1:
        print("Out of range :", score, "\n")
    elif score >= 0.9:
        print("A\n")
    elif score >= 0.8:
        print("B\n")
    elif score >= 0.7:
        print("C\n")
    elif score >= 0.6:
        print("D\n")
    else:
        print("F\n")
