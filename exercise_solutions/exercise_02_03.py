print('Think of a number between 1 and 99')
low = 0
high = 100

while True:
    middle = round((high - low) / 2) + low
    print('{} {} {}'.format(low, middle, high))
    if middle == high or middle == low:
        break
    answer = input('Is the number greater than ' + str(middle))
    if (answer == 'y'):
        low = middle
    else:
        high = middle
    

print('Your number is ' + str(high))