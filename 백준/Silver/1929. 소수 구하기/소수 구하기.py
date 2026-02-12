import math

def is_prime_number(n):
    # 1은 소수가 아님
    if n < 2:
        return False
    
    # 2부터 n의 제곱근까지 나누어떨어지는지 확인
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False # 소수가 아님
    return True # 소수임

m, n = map(int, input().split())

for i in range(m, n + 1):
    if is_prime_number(i):
        print(i)