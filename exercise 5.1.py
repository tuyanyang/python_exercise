total = 0
count = 0
while True:
    nStr = input('Enter a number: ')
    try:
        if nStr == 'done':
            break
        n = float(nStr)
        total += n
        count += 1
    except:
        print('Invalid input')
        continue
print(total,count, total/count)