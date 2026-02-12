import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
x = deque([])

for _ in range(n):
    cm = input().split()
    if cm[0] == "push":
        x.append(cm[1])
    elif cm[0] == "pop":
        if not x:
            print(-1)
        else:
            print(x.popleft())
    elif cm[0] == "size":
        print(len(x))
    elif cm[0] == "empty":
        print("0" if x else "1")
    elif cm[0] == "front":
        print(x[0] if x else "-1")
    elif cm[0] == "back":
        print(x[-1] if x else "-1")