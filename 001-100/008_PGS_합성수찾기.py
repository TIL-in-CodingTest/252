def solution(n):
    answer = 0
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    # 에라토스테네스의 체를 통해 소수를 찾아내기
    for i in range(2, int(n**0.5) + 1): # 2부터 n의 제곱근까지의 범위
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    answer = sum(1 for prime in is_prime[2:n + 1] if not prime) # 소수가 아닌 숫자마다 1을 생성한 후 합산
    
    return answer


# 에라토스테네스의 체: 소수를 찾는 알고리즘

# 2부터 시작해서 지워지지 않은 가장 작은 수를 찾습니다. 이 수는 소수입니다.
# 찾은 소수의 배수를 모두 지웁니다. (이때, 이미 지워진 수는 무시합니다.)
# 이 과정을 반복합니다. 이렇게 반복하면 지워지지 않은 수들은 모두 소수가 됩니다.