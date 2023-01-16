titles = []

while True:
    new_title = input('Enter a file title: ')
    if len(new_title) == 0:
        break
    titles.append(new_title)
    print(titles)