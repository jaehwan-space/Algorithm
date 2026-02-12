from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    prio = list(map(int, input().split()))
    q = deque()
    
    for i in range(n):
        q.append((prio[i], i))
        
    count = 0
    
    while q:
        current = q.popleft()
        if any(current[0] < qu[0] for qu in q):
            q.append(current)
        else:
            count += 1
            if current[1] == m:
                print(count)
                break