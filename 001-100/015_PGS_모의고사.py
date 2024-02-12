def count(supo_answer, answers):
    count = 0
    
    for i in range(len(answers)):
        if answers[i] == supo_answer[(i+1) % len(supo_answer) - 1]:
            count += 1
    
    return count

def solution(answers):
    answer = []
    counts = []
    
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    counts.append(count(supo1, answers))
    counts.append(count(supo2, answers))
    counts.append(count(supo3, answers))
    
    max_value = max(counts)
    answer = [i + 1 for i, value in enumerate(counts) if value == max_value]
    
    return answer