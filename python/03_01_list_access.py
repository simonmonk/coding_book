titles = ['Jaws', 'The Godfather', 'Baby Driver', 'Inception']
num_titles = len(titles)

while True:
    index_str = input('Enter index number: ')
    index = int(index_str)
    if index >= 0 and index < len(titles):
        print(titles[index])
    else:
        print('Index must be between 0 and ' + str(num_titles))