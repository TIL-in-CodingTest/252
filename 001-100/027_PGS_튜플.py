import re
from collections import Counter

def solution(s):
    answer = []
    # temp = {}
    
    # for i in s.split(','):
    #     i = re.findall(r'\d+', i)[0]
    #     if i in temp:
    #         temp[i] += 1
    #     else:
    #         temp[i] = 1
    s = Counter(re.findall('\d+', s)) # Counter 객체를 활용하여 위 과정을 표현할 수 있다.
            
    answer = [int(key) for key, value in sorted(s.items(), key=lambda item: item[1], reverse=True)]
    
    return answer

# 딕셔너리 -> 숫자를 키로 추가, 초기값은 1 -> 숫자가 등장한 횟수만큼 값을 늘려준다. 값의 내림차순으로 정렬한 결과가 답이다.