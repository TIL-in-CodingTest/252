from functools import cmp_to_key

def compare(x, y):
    
    # x와 y를 이어붙였을 때 큰 수가 나오도록 비교
    return int(y + x) - int(x + y)

def solution(numbers):

    # 비교 함수를 이용하여 배열 정렬
    sorted_nums = sorted(map(str, numbers), key=cmp_to_key(compare))
    
    answer = ''.join(sorted_nums)
    
    if sorted_nums[0] == '0':
        return '0'
    
    return answer