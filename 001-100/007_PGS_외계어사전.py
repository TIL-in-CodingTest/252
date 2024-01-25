def solution(spell, dic):
    answer = 2
    
    for word in dic:
        if all(char in word for char in spell):
            answer = 1
    
    return answer