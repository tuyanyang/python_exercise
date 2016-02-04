h = input('Enter Hours: ')
Hours = int(h)
r = input('Enter Rate: ')
Rate = int(r)


def computepay(hours,rate):
    if hours <= 40:
        pay = hours*rate
    else:
        pay = 1.5*hours*rate-0.5*40*rate
    return pay

Pay = computepay(Hours, Rate)
print('Pay: ',Pay)
