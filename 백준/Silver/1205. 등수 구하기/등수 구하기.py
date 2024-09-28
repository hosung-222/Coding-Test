n, score, p = map(int, input().split()) 
if n > 0:
    score_board = list(map(int, input().split()))
    if n == p and score_board[-1] >= score:
        print(-1)
    else:
        rank = n + 1
        for i in range(n):
            if score_board[i] <= score:
                rank = i + 1
                break

        print(rank)
else:
    print(1)