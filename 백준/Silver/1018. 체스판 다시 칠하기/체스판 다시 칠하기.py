N,M = map(int,input().split())
tile = [list(input()) for _ in range(N)]

result = N*M

for chess_row in range(N-7):
    for chess_col in range(M-7):
        new_tile = [[tile[row][col] for col in range(chess_col, chess_col+8)] for row in range(chess_row, chess_row+8)]
        cnt_1,cnt_2 = 0,0
        for i in range(len(new_tile)):
            for j in range(len(new_tile[i])):
                if (i+j)%2 == 0:
                    if (new_tile[i][j] != 'W'):
                        cnt_1 += 1
                    else:
                        cnt_2 += 1

                else:
                    if (new_tile[i][j] != 'B'):
                        cnt_1 += 1
                    else:
                        cnt_2 += 1

        result = min(cnt_1, cnt_2, result)
    

print(result)