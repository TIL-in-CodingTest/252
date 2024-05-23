def solution(nums):
    answer = 0
    
    if len(set(nums)) >= len(nums)/2:
        answer = len(nums)/2
    else:
        answer = len(set(nums))
        
    return answer

# nums: N마리 폰켓몬의 종류 번호
# answer: 가장 많은 종류의 폰켓몬 N/2마리를 선택했을 때 종류의 개수