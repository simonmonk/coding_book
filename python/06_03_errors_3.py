x_str = input('Enter a number: ')
try:
    x = int(x_str)
    y = x * x
    print(y)
except:
    print('You must enter a number')