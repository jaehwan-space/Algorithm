import sys
from collections import deque
input = sys.stdin.readline

x = deque([])
n = int(input())

for _ in range(n):
    cm = input().rstrip().split(" ")
    if cm[0] == "push":
        x.append(cm[1])
    elif cm[0] == "pop":
        if not x:
            print(-1)
        else:
            print(x.pop())
    elif cm[0] == "size":
        print(len(x))
    elif cm[0] == "empty":
        if not x:
            print(1)
        else:
            print(0)
    elif cm[0] == "top":
        if not x:
            print(-1)
        else:
            print(x[-1])