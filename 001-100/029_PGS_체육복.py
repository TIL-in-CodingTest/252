def solution(n, lost, reserve):
    answer = n
    lost.sort()
    reserve.sort()
    
    # 여분 체육복이 있는 학생이 도난을 당한 경우
    lost2 = [x for x in lost if x not in reserve]
    reserve = [x for x in reserve if x not in lost]
            
    for i in lost2:
        if i-1 in reserve: 
            # del reserve[reserve.index(i-1)]
            reserve.remove(i-1)
        elif i+1 in reserve:
            reserve.remove(i+1)
        else:
            answer -= 1
            
    return answer

# 바로 앞번호나 바로 뒷번호 학생에게만 체육복을 빌려줄 수 있다.
# n: 전체 학생 수, lost: 체육복을 도난 당한 학생의 번호 배열, reserve: 체육복을 빌려줄 수 있는 학생의 번호 배열
# answer: 체육복이 있는 학생의 최댓값
# 여벌 체육복을 가져온 학생도 도난을 당할 수 있다. 하나만 도난당했다고 가정, 빌려줄 수 없게 된다.