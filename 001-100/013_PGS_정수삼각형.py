from collections import defaultdict
# defaultdict은 존재하지 않는 키에 접근할 때 예외를 발생시키지 않고, 기본값을 반환한다.


def solution(triangle):
    answer = defaultdict(int)
    answer[(0,0)] = triangle[0][0]

    for x in range(1, len(triangle)):
        for y in range(len(triangle[x])):
            answer[(x,y)] = triangle[x][y] + max(answer[(x-1,y-1)], answer[(x-1,y)])

    return max(answer.values())