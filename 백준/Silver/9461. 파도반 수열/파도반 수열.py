import sys
input = sys.stdin.readline

t = int(input())
cases = [int(input()) for _ in range(t)]
dp = [0] * (max(cases) + 1)

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for i in range(6, max(cases) + 1):
    dp[i] = dp[i - 1] + dp[i - 5]

for i in cases:
    print(dp[i])