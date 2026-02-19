import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)], reverse=True)
result = 0

for i in coins:
    if k // i > 0:
        result += (k // i)
        k %= i
        
print(result)