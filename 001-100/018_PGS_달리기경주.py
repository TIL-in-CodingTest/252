def solution(players, callings):

    # 선수 이름과 인덱스를 저장하는 딕셔너리 생성
    player_dict = {key: i for i, key in enumerate(players)}
    
    for calling in callings:

        index = player_dict[calling]  # 딕셔너리에서 호출된 선수의 인덱스를 가져옴
        players[index], players[index - 1] = players[index - 1], players[index]
        
        # 딕셔너리 업데이트
        player_dict[calling] -= 1
        player_dict[players[index]] += 1
    
    return players

# 이름을 부른다 -> 이름이 불린 선수와 그 선수 앞에 위치한 선수의 순서가 바뀐다.
# players: 현재 등수 순서대로 이름이 담김
# callings: 해설진이 부른 이름이 담김