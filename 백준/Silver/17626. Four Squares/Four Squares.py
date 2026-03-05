import sys
input = sys.stdin.readline

n = int(input())

# 1개 제곱수
if int(n**0.5)**2 == n:
    print(1)
    exit()

# 4개 판별 (르장드르 정리)
tmp = n
while tmp % 4 == 0:
    tmp //= 4

if tmp % 8 == 7:
    print(4)
    exit()

# 2개 판별
for i in range(1, int(n**0.5) + 1):
    if int((n - i*i)**0.5)**2 == n - i*i:
        print(2)
        exit()

# 나머지
print(3)