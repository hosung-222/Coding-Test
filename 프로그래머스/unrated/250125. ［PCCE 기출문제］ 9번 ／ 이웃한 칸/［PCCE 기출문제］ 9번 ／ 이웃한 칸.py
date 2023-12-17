def solution(board, h, w):
    answer = 0
    color = board[h][w]
    dh = [-1,1,0,0]
    dw = [0,0,-1,1]
    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        if nh>=0 and nh<len(board) and nw>=0 and nw<len(board[0]):
            if color == board[nh][nw]:
                answer += 1
    
    return answer