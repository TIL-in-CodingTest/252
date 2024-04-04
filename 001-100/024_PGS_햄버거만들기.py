def solution(ingredient):
    answer = 0
    pattern = [1, 2, 3, 1]  # 제거할 패턴
    idx = 0  # 리스트 인덱스 초기화

    while idx < len(ingredient):
        if ingredient[idx:idx+len(pattern)] == pattern:  # 패턴과 일치하는 부분 찾기
            del ingredient[idx:idx+len(pattern)]  # 패턴 제거
            answer += 1
            idx -= len(pattern)  # 다음 패턴 검사를 위해 인덱스 조정
        else:
            idx += 1  # 다음 인덱스로 이동
    
    return answer

# 햄버거 포장 순서: 아래서부터 (1)빵-(2)야채-(3)고기-(1)빵