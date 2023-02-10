import random

board = ['.', '.', '.',
         '.', '.', '.',
         '.', '.', '.']

turn = 'x'

lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], # horizontal
         [0, 3, 6], [1, 4, 7], [2, 5, 8], # vertical
         [0, 4, 8], [2, 4, 6]]            # diagonal

def show_board():
    print()
    print(board[0] + '|' + board[1] + '|' + board[2] + '   1|2|3')
    print('----   ----')
    print(board[3] + '|' + board[4] + '|' + board[5] + '   4|5|6')
    print('----   ----')
    print(board[6] + '|' + board[7] + '|' + board[8] + '   7|8|9')
    print()
    
def check_winner():
    winner = '.' # no one
    for line in lines:
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
    move = -1
    if turn == 'x':
        move = get_move_person()
    else:
        move = get_move_automatic()
        if move != -1:
            print(turn + ' moves: ' + str(move))
    return move

def get_move_person():
    position = -1 # un-chosen / no move available
    moves = allowed_moves()
    if len(moves) > 0:
        while position == -1:
            print()
            p_str = input('Move for ' + turn + str(moves) + ' :')
            p = int(p_str)
            if p in moves:
                position = p 
    return position

def is_winning_move(board_position, turn):
    result = False
    old_contents = board[board_position-1]
    board[board_position-1] = turn
    for line in lines:
        if board[line[0]] == board[line[1]] == board[line[2]]:
            if board[line[0]] == turn:
                result = True
                break
    board[board_position-1] =  old_contents # put it back
    return result

def get_move_automatic():
    moves = allowed_moves()
    if len(moves) == 0:
        return -1
    # look for winning move
    for move in moves:
        if is_winning_move(move, 'o'):
            return move
    # look for blocking move
    for move in moves:
        if is_winning_move(move, 'x'):
            return move
    return random.choice(moves)

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