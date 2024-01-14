from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([(p, i) for i, p in enumerate(priorities)])

    while queue:
        current_priority, current_idx = queue.popleft()

        if any(current_priority < priority for priority, _ in queue):
            # 대기 중인 프로세스 중 현재 프로세스보다 높은 우선순위가 있는 경우
            queue.append((current_priority, current_idx))
        else:
            answer += 1
            if current_idx == location:
                return answer