from itertools import permutations

def solution(k, dungeons):

    all_dungeons = []
    possible = []
    
    # 모든 탐험 순서 도출
    for i in permutations(dungeons):
        all_dungeons.append(list(i))
    
    # 가능한 탐험 순서 도출
    for i in range(len(all_dungeons)):
        temp_k = k
        count = 0
        for d in all_dungeons[i]:
            if temp_k >= d[0]:
                temp_k -= d[1]
                count += 1
            elif temp_k < d[0]:
                break

        possible.append(count)

    answer = max(possible)      
    return answer

# k: 현재 피로도, dungeons: [최소 필요 피로도, 소모 피로도]
# answer: 유저가 탐험할 수 있는 최대 던전 수