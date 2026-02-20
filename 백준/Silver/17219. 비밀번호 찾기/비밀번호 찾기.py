import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pw = {}
for _ in range(n):
    k, v = map(str, input().rstrip().split())
    pw[k] = v

for _ in range(m):
    target = input().rstrip()
    print(pw[target])