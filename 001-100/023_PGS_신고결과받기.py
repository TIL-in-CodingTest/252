def solution(id_list, report, k):
    answer = []
    
    mailed_id = {id : 0 for id in id_list} # key: 전체 id, value: 메일 받은 횟수
    report = list(set(report)) # 중복 제거
    reported_id = {}

    for id in report:
        value, key = id.split() # key: 신고 받은 id, value: 신고한 id
        if key in reported_id:
            reported_id[key].append(value)
        else:
            reported_id[key] = [value]
    
    for id in id_list:
        if id in reported_id and len(reported_id[id]) >= k:
            for id in reported_id[id]:
                mailed_id[id] += 1
    
    answer = list(mailed_id.values())
    
    return answer

# k번 이상 신고된 유저는 이용 정지, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송
# answer: 각 유저 별로 처리 결과 메일을 받은 횟수 (id_list에 담긴 순서대로)