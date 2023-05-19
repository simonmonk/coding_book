board = ['.', '.', '.',
         '.', '.', '.',
         '.', '.', '.']

turn = 'x'

winning_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], # horizontal
         [0, 3, 6], [1, 4, 7], [2, 5, 8], # vertical
         [0, 4, 8], [2, 4, 6]]            # diagonal

def show_board():
    print(board[0] + board[1] + board[2] + ' 123')
    print(board[3] + board[4] + board[5] + ' 456')
    print(board[6] + board[7] + board[8] + ' 789')
    
def check_winner():
    winner = '.' # no one
    for line in winning_lines:
        if board[line[0]] == board[line[1]] == board[line[2]]:
            winner = board[line[0]]
            break
    return winner

def allowed_moves():
    moves = []
    for move in range(1, 10):
        if board[move-1] == '.':
            moves.append(move)
    return moves

def get_move():
    position = -1 # un-chosen / no move available
    moves = allowed_moves()
    if len(moves) > 0:
        while position == -1:
            p_str = input('Move for ' + turn + str(moves) + ' :')
            p = int(p_str)
            if p in moves:
                position = p 
    return position

show_board()

while True:
    position = get_move()
    if position == -1:
        print("Its a tie")
        break
    else:
        board[position-1] = turn
    show_board()
    winner = check_winner()
    if  winner != '.':
        print(winner + ' wins!')
        break
    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'