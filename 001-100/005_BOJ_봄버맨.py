import sys

def bomb(data):
    updated_data = [['O' for _ in range(c)] for _ in range(r)]

    for i in range(r):
            for j in range(c):
                if data[i][j] == 'O':
                    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1), (i, j)]:
                        if 0 <= x < r and 0 <= y < c:
                            updated_data[x][y] = '.'
    return updated_data

input = sys.stdin.readline

r, c, n = map(int, input().split())
initial_state = [list(input().strip()) for _ in range(r)]

if n <= 1:
    print('\n'.join(''.join(r) for r in initial_state))

elif n % 2 == 0: # 짝수 초에는 전체가 폭탄이다.
    print('\n'.join('O' * c for _ in range(r)))

elif n % 4 == 3: # 초기 상태의 폭탄이 터지는 경우다.
    answer = bomb(initial_state)
    print('\n'.join(''.join(r) for r in answer))

elif n % 4 == 1:
    answer = bomb(bomb(initial_state))
    print('\n'.join(''.join(r) for r in answer))
