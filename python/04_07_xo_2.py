board = ['.', '.', '.',
         '.', '.', '.',
         '.', '.', '.']

turn = 'x'

def show_board():
    print(board[0] + board[1] + board[2] + ' 123')
    print(board[3] + board[4] + board[5] + ' 456')
    print(board[6] + board[7] + board[8] + ' 789')
    
show_board()

while True:
    position_str = input('Move for ' + turn + ' :')
    position = int(position_str)
    board[position - 1] = turn
    show_board()
    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'
