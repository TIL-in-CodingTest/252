import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(answer) # participant에는 있지만 completion에는 없는 요소들과 그 개수 반환
    return list(answer.keys())[0]

# 다른 코드
# def solution(participant, completion):
#     answer = ''
#     temp = 0
#     dic = {}
#     for part in participant:
#         dic[hash(part)] = part # key: 참가자의 해시값, value: 참가자의 이름
#         temp += int(hash(part))
#     for com in completion:
#         temp -= hash(com) # 참가자 해시값의 합 - 완주자 해시값
#     answer = dic[temp]

#     return answer