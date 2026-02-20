import sys
input = sys.stdin.readline
    
t = int(input())
m = [int(input()) for _ in range(t)]

n = max(m)
dp = [[0, 0] for _ in range(n + 2)]
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, n + 1):
    dp[i] = [dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1]]
    
for i in m:
    print(*dp[i])