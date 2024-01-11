def solution(prices):
    
    n = len(prices)
    answer = [0] * n  # 리스트 초기화

    stack = []  # 인덱스 저장
    for i in range(n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    # 스택에 남아있는 인덱스들은 끝까지 가격이 떨어지지 않은 경우이므로 처리
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j

    return answer