H=input('Enter Hours: ')
try:
    Hours=int(H)
    R=input('Enter Rate; ')
    try:
        Rate=int(R)
        if Hours>40:
            Pay=1.5*Rate*Hours-0.5*40*Rate
        else:
            Pay=Rate*Hours
        print('Pay: ',Pay)
    except:
        print('Error, please enter numeric input')
except:
    print('Error, please enter numeric input')