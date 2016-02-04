while True:
    sa = input("Input score a between 0.0 and 1.0:")
    try:
        a = float(sa)
    except ValueError:
        print("Bad score a")
        continue

    sb = input("Input score b between 0.0 and 1.0:")
    try:
        b = float(sb)
    except ValueError:
        print("Bad score b")
        continue

    c=a+b
    print(a,"+",b,"=",c,"\n")