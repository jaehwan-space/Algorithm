import sys
input = sys.stdin.readline

s = set()
n = int(input())

for _ in range(n):
    m = input().split()
    if m[0] == "add":
        s.add(int(m[1]))
    elif m[0] == "remove":
        s.discard(int(m[1]))
    elif m[0] == "check":
        if int(m[1]) in s:
            print(1)
        else:
            print(0)
    elif m[0] == "toggle":
        if int(m[1]) in s:
            s.discard(int(m[1]))
        else:
            s.add(int(m[1]))
    elif m[0] == "all":
        s = set(list(range(1, 21)))
    elif m[0] == "empty":
        s = set()