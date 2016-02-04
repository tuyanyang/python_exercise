nums = list()
while True:
    nStr = input('Enter a number: ')
    try:
        if nStr == 'done':
            break
        n = float(nStr)
        nums.append(n)
    except:
        print('Invalid input')
        continue
print('Maximum: ',max(nums))
print('Minimum: ',min(nums))