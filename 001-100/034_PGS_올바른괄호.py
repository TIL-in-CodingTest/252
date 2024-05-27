def solution(s):
    
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                return False
    
    return len(stack) == 0

# (를 일단 넣고, 짝을 찾으면 pop한다. 문자열을 모두 순회했는데 스택이 비어있지 않다면 False