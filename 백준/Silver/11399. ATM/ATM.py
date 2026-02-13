import sys
input = sys.stdin.readline

n = int(input())
time = sorted(list(map(int, input().split())))
result = 0

for i in range(n):
    result += time[i] * abs(i - n)

print(result)