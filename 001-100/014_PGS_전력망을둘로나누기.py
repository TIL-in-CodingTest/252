from collections import deque

def make_graph(wires, n):
    graph = {i: [] for i in range(1, n + 1)}
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    return graph

def bfs(graph, start, removed_node, visited):
    queue = deque([start])
    visited[start] = True
    count = 1  # 시작 노드도 포함하기 때문에 1로 초기화

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i] and i != removed_node:
                queue.append(i)
                visited[i] = True
                count += 1

    return count

def solution(n, wires):
    answer = float('inf')

    for wire in wires:
        graph = make_graph(wires, n)

        # 간선을 하나씩 제거한 경우의 전력망 크기 계산
        a, b = wire
        visited = [False] * (n + 1)
        count_a = bfs(graph, a, b, visited)
        count_b = n - count_a  # 전체 노드 수에서 A 전력망 크기를 뺌

        # 최소 차이 갱신
        diff = abs(count_a - count_b)
        answer = min(answer, diff)

    return answer