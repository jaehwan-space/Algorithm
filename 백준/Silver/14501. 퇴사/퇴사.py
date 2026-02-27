import sys
input = sys.stdin.readline

n = int(input())
schedule = [0] + [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 2)

for i in range(n,0,-1):
    t, p = schedule[i]
    if i + t <= n + 1:
        dp[i] = max(dp[i + 1], p + dp[i + t])
    else:
        dp[i] = dp[i + 1]   
print(dp[1])