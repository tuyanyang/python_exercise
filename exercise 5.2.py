largest = None
smallest = None
while True:
    nStr = input('Enter a number: ')
    try:
        if nStr == 'done':
            break
        n = float(nStr)
        if largest is None or largest < n:
            largest = n
        if smallest is None or smallest > n:
            smallest = n
    except:
        print('Invalid input')
        continue
print('Largest: ', largest)
print('Smallest: ', smallest)