import itertools

def solution(numbers):
    answer = count_prime_combinations(numbers)
    return answer

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_prime_combinations(numbers):
    permutations = []
    prime_count = 0
    
    for i in range(1, len(numbers) + 1): # 자릿수
        for p in itertools.permutations(numbers, i):
            permutations.append(int(''.join(p)))
            
    for p in set(permutations):
        if is_prime(p):
            prime_count += 1
    
    return prime_count

# 한자리 숫자가 적힌 종이 조각을 붙여 만들 수 있는 소수의 개수