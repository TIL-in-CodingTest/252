import math
from datetime import datetime

def solution(fees, records):
    answer = []
    code_records = {}

    for record in records:
        time, code, status = record.split()
        
        if code not in code_records:
            code_records[code] = []
            
        code_records[code].append((time, status))

    sorted_codes = sorted(code_records.keys())
    
    for code in sorted_codes:
        records = code_records[code]
        records.sort()
        
        total_minutes = 0

        while records:
            in_time, _ = records.pop(0)
            out_time, _ = records.pop(0) if records else ("23:59", "OUT")

            # 누적 시간 계산
            time_format = "%H:%M"
            time1 = datetime.strptime(in_time, time_format)
            time2 = datetime.strptime(out_time, time_format)
            time_difference = time2 - time1
            total_minutes += time_difference.total_seconds() / 60

        # 주차 요금 계산
        if total_minutes > fees[0]:
            fee = fees[1] + math.ceil((total_minutes - fees[0]) / fees[2]) * fees[3]
        else:
            fee = fees[1]

        answer.append(fee)

    return answer