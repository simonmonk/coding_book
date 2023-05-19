board = ['.', '.', '.',
         '.', '.', '.',
         'x', 'x', 'x']

winning_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], # horizontal
         [0, 3, 6], [1, 4, 7], [2, 5, 8], # vertical
         [0, 4, 8], [2, 4, 6]]            # diagonal


# buggy original check_winner function. 
def check_winner1():
    winner = '.' # no one
    for line in winning_lines:
        if board[line[0]] == board[line[1]] == board[line[2]]:
            winner = board[line[0]]
            break
    return winner

# fixed - only check for rows of x or o
def check_winner2():
    winner = '.' # no one
    for line in winning_lines:
        if board[line[0]] != '.' and (board[line[0]] == board[line[1]] == board[line[2]]):
            winner = board[line[0]]
            break
    return winner

print(check_winner1())
print(check_winner2())