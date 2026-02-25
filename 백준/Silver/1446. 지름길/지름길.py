import sys
input = sys.stdin.readline
INF = int(1e9)

n, d = map(int, input().split())
road = [INF] * (d + 1)
shortcut = [[] for _ in range(d + 1)]

for _ in range(n):
    start, end, dist = map(int, input().split())
    if end <= d:
        shortcut[start].append((end, dist))
    
road[0] = 0
for i in range(d):
    road[i + 1] = min(road[i + 1], road[i] + 1)
    
    for end, dist in shortcut[i]:
        road[end] = min(road[end], road[i] + dist)
    
print(road[d])