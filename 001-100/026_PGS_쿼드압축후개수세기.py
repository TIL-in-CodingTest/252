def solution(arr):
    answer = []

    def is_same(row_start, row_end, col_start, col_end):
            ref = arr[row_start][col_start]
            for i in range(row_start, row_end):
                for j in range(col_start, col_end):
                    if arr[i][j] != ref:
                        return False
            return True
        
    def quad_tree(row_start, row_end, col_start, col_end):
        # 해당 범위가 모두 같은 숫자로 이루어져 있으면 해당 숫자 반환
        if is_same(row_start, row_end, col_start, col_end):
            return str(arr[row_start][col_start])

        # 그렇지 않다면, 범위를 4분할하여 재귀적으로 호출
        mid_row = (row_start + row_end) // 2
        mid_col = (col_start + col_end) // 2
        result = "("
        result += quad_tree(row_start, mid_row, col_start, mid_col)  # 왼쪽 상단
        result += quad_tree(row_start, mid_row, mid_col, col_end)    # 오른쪽 상단
        result += quad_tree(mid_row, row_end, col_start, mid_col)    # 왼쪽 하단
        result += quad_tree(mid_row, row_end, mid_col, col_end)      # 오른쪽 하단
        result += ")"
        return result
    
    arr = quad_tree(0, len(arr), 0, len(arr)) # 재귀적으로 배열을 분할할 때 마지막 인덱스를 포함하기 위해 len(arr)을 사용
    
    answer.append(arr.count('0'))
    answer.append(arr.count('1'))
    
    return answer