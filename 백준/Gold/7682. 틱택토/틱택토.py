def is_valid_state(board):
    x_count = board.count('X')
    o_count = board.count('O')
    
    matrix = [list(board[i*3: (i+1)*3]) for i in range(3)]

    def check_winner(player):
        for i in range(3):
            if all([matrix[i][j] == player for j in range(3)]):
                return True
            elif all([matrix[j][i] == player for j in range(3)]):
                return True
        
        if all([matrix[i][i] == player for i in range(3)]):
            return True
        
        elif all(matrix[i][2-i] == player for i in range(3)):
            return True
        return False
    
    x_win = check_winner("X")
    o_win = check_winner("O")

    if o_count > x_count or x_count - o_count > 1:
        return False
    
    if x_win and o_win:
        return False
    
    if x_win:
        if x_count - o_count != 1:
            return False
        return True

    if o_win:
        if x_count != o_count:
            return False
        return True

    if x_count + o_count == 9:
        return True
    
    return False


while True:
    board = input().strip()
    if board == 'end':
        break
    if is_valid_state(board):
        print('valid')
    else:
        print('invalid')

