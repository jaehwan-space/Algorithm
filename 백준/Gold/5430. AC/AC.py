import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    cmd = input().rstrip()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(","))
    result = True
    re = 0
    for i in cmd:
        if i == "R":
            re += 1
        elif i == "D":
            if n == 0:
                result = False
                break
            if re % 2 == 0:
                arr.popleft()
            else:
                arr.pop()
            n -= 1
    if result:
        if re % 2 == 1:
            arr.reverse()
        print(f"[{','.join(arr)}]")
    else:
        print("error")