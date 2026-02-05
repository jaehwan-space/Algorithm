import sys
input = sys.stdin.readline
d = [0] * 10001

n = int(input())
for _ in range(n):
    d[int(input())] += 1

for i in range(1, 10001):
    for j in range(d[i]):
        print(i)
        