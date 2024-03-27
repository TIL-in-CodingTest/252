def solution(today, terms, privacies):
    answer = []
    index = 0
    term_dict = {}
    
    for term in terms:
        key, value = term.split()
        term_dict[key] = int(value)  # 알파벳은 키, 숫자는 값
    
    # 파기 시작 날짜 도출
    end_dates = []
    
    for p in privacies:
        available_month = int(term_dict[p[-1]])
        year = int(p[:4])
        month = int(p[5:7])
        day = p[8:10]
        
        year += (month + available_month) // 12
        month = (month + available_month) % 12
        
        if month == 0:
            month = 12
            year -= 1
        
        end_date = str(year) + str(month).zfill(2) + day.zfill(2)
        end_dates.append(end_date)
        
    # 오늘 날짜와 파기 시작 날짜를 비교하여 파기 여부 확인
    for date in end_dates:
        index += 1
        if int(today.replace(".", "")) >= int(date):
            answer.append(index)
            print(answer)
    
    return answer