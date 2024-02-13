def solution(a, b):
    answer = ''
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    count = 0
    
    for i in range(a - 1):
        count += days[i]
    count += b
    
    answer = week[(count % 7) - 1]
    
    return answer