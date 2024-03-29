import re

def solution(new_id):
    
    # st = st.lower()
    # st = re.sub('[^a-z0-9\-_.]', '', st)
    # st = re.sub('\.+', '.', st)
    # st = re.sub('^[.]|[.]$', '', st)
    # st = 'a' if len(st) == 0 else st[:15]
    # st = re.sub('^[.]|[.]$', '', st)
    # st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    
    answer = ''
    available_char = r'[a-z0-9\-_\.]+'
    
    # 1단계: 대문자 -> 소문자    
    # 2단계: 사용 가능한 문자를 제외한 모든 문자 제거 (available_char과 매칭되는 부분 반환)
    new_id = re.findall(available_char, new_id.lower())
    new_id = ''.join(new_id)
    
    # 3단계: 마침표 연속된 부분 하나로 치환
    new_id = re.sub(r'\.{2,}', '.', new_id) # {n,}: 앞선 패턴이 n회 이상 반복
    
    # 4단계: 처음과 끝에 위치한 마침표 제거
    new_id = re.sub(r'^\.|\.$', '', new_id)
    
    # (5) 빈 문자열일 경우 a 대입
    new_id = new_id if new_id else 'a'
    
    # (6) 16자 이상이면 첫 15개 문자를 제외하고 제거, 제거 후 마침표가 끝에 위치한다면 그것도 제거
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    # (7) 2자 이하라면 마지막 문자를 길이가 3이될 때까지 반복해서 끝에 붙이기
    elif len(new_id) < 3:
        last_char = new_id[-1]
        while len(new_id) < 3:
            new_id += last_char
    
    answer = new_id
    
    return answer

# 아이디 규칙에 맞지 않는 아이디 -> 유사하면서 규칙에 맞는 아이디를 추천
# 3자 이상 15자 이하, 소문자, 숫자, -, _, .만 사용 가능
# .는 연속으로/처음과 끝에 사용 불가

# new_id: 신규 유저 입력한 아이디
# answer: 7단계를 거친 추천 아이디