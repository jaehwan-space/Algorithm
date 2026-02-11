import sys
input = sys.stdin.readline

n = int(input())
lists = [int(input()) for _ in range(n)]
lists.sort()
for i in lists:
    print(i)