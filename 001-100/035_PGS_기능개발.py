import math

def solution(progresses, speeds):
    date = [] # 배포 가능한 날짜 넣기
    answer = [] 
    
    for i in range(len(progresses)):
        date.append(math.ceil((100 - progresses[i]) / speeds[i]))
        
    while date:
        temp = date.pop(0)
        deploy = 1
        
        while date and temp >= date[0]:
            date.pop(0)
            deploy += 1
        
        answer.append(deploy)
    
    return answer

# progresses: 작업 진도 (배포순)
# speeds: 각 작업의 개발 속도
# answer: 각 배포마다 배포되는 기능 수, 앞의 기능이 완성되지 않으면 배포 불가