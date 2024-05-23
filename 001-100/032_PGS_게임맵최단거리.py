from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])

    visited = [[0 for _ in range(m)] for _ in range(n)]
    dq = deque()
    dq.append((0,0))
    dx, dy = [1,0,-1,0], [0,1,0,-1]

    while dq:
        x, y = dq.popleft() # 캐릭터의 위치
        visited[x][y] = 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] # 이동할 수 있는 위치
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    dq.append((nx,ny)) # 갈 수 있는 길이라면 큐에 추가
                    maps[nx][ny] = maps[x][y] + 1

    if visited[n-1][m-1]: # 최단 경로가 답이 된다.
        answer = maps[n-1][m-1]
        return answer
    else:
        return -1

# 동서남북으로 한 칸씩 이동 가능
# answer: 상대 팀 진영에 도착하기 위해서 지나야 하는 칸 개수의 최솟값

# DFS: 성공 및 실패 여부와 관계없이 하나의 경로를 끝까지 탐색한다.
# BFS: 여러 경로를 한 단계씩 탐색하여 짧은 경로에 가장 먼저 도달한다.