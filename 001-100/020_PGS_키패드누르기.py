def solution(numbers, hand):
    answer = ''
    left_hand = (3, 0)  # 초기 왼손 위치
    right_hand = (3, 2)  # 초기 오른손 위치
    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
              4: (1, 0), 5: (1, 1), 6: (1, 2),
              7: (2, 0), 8: (2, 1), 9: (2, 2),
              0: (3, 1)}
    
    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            left_hand = keypad[n]
        elif n in [3, 6, 9]:
            answer += 'R'
            right_hand = keypad[n]
        else:
            left_distance = calculate_distance(keypad[n], left_hand)
            right_distance = calculate_distance(keypad[n], right_hand)
            if left_distance < right_distance or (left_distance == right_distance and hand == "left"):
                answer += 'L'
                left_hand = keypad[n]
            else:
                answer += 'R'
                right_hand = keypad[n]
    
    return answer
            
def calculate_distance(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

# 왼손: *, 1, 4, 7
# 오른손: #, 3, 6, 9
# 위치가 가까운 손가락: 2, 5, 8, 0 (위치가 같을 경우 오른손잡이는 오른손, 왼손잡이는 왼손)
# numbers: 누를 번호가 담긴 배열
# hand: 왼손잡이인지 오른손잡이인지 나타내는 문자열 (left or right)
# answer: 각 번호를 누른 손가락이 어느 손인지 나타내는 문자열 (L or R)

# 3*4크기의 2차원 배열을 만들고, 각 엄지의 위치를 나타낸다. -> 배열 대신 딕셔너리로 구현
# 각 위치에서 상하좌우에 L 또는 R이 있는지 확인? -> not efficient
#             while True:
#                 d = 1 # distance
                
#                 for x, y in [(n+d, d), (n-d, d), (n, d+1), (n, d-1), (n, 1)]:
#                     if 0 <= x < 3 and 0 <= y < 4:
#                         if keypad[x][y] == 'L':