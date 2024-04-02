def solution(survey, choices):
    answer = ''
    
    type = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(choices)):
        if choices[i] in (1, 2, 3): # 점수 3,2,1
            type[survey[i][0]] += abs(choices[i] - 4)
        elif choices[i] in (5, 6, 7): # 점수 1,2,3
            type[survey[i][1]] += choices[i] - 4
            
    answer += 'R' if type['R'] >= type['T'] else 'T'
    answer += 'C' if type['C'] >= type['F'] else 'F'
    answer += 'J' if type['J'] >= type['M'] else 'M'
    answer += 'A' if type['A'] >= type['N'] else 'N'
    
    return answer

# 16가지 성격 유형
# 질문 n개, 선택지 7개: 매우 동의/매우 비동의 3점, 동의/비동의 2점, 약간 동의/약간 비동의 1점
# 하나의 지표에서 각 성격 유형 점수가 같으면, 두 성격 유형 중 사전 순으로 빠른 성격 유형 선택
# survey: 질문마다 판단하는 지표 ("RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA")
# choices: 선택한 선택지 배열 (1~7)
# choices 1, 2, 3 -> survey[i][0], choices 4, 5, 6 -> survey[i][1]