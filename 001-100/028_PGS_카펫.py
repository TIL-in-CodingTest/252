def solution(brown, yellow):
    answer = []
    
    total = brown + yellow
    
    # 완전탐색
    for width in range(1, total+1):
        if total % width == 0:
            height = total // width
            if width >= height and (width + height) * 2 - 4 == brown:
                answer.extend([width, height])
                break
    
    return answer


# 테두리 1줄은 갈색, 나머지 노란색
# brown = (가로+세로)*2 - 4 
# brown + yellow = 가로 * 세로
# 카펫 가로 >= 세로