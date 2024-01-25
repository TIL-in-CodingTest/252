def solution(board):
    answer = 0
    
    row = len(board)
    col = len(board[0])
    
    updated_board = [[0 for _ in range(col)] for _ in range(row)]
    
    for i in range(row):
            for j in range(col):
                if board[i][j] == 1:
                    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1), (i-1, j-1), (i+1, j+1), (i+1, j-1), (i-1, j+1), (i, j)]:
                        if 0 <= x < row and 0 <= y < col:
                            updated_board[x][y] = 1
                            
    print(updated_board)
    answer = sum(row.count(0) for row in updated_board)
    
    return answer