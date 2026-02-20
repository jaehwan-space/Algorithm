from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] * n for _ in range(n)]
visited = [[] * n for _ in range(n)]

for i in range(n):
    d = list(map(int, input().split()))
    for j in range(n):
        if d[j] == 1:
            graph[i].append(j)
            
def bfs(arr, v, visit):
    q = deque(graph[v])
    while q:
        target = q.popleft()
        if target in visit[v]:
            continue
        visit[v].append(target)
        q.extend(graph[target])

for i in range(n):
    bfs(graph, i, visited)
    
for i in range(n):
    row = []
    for j in range(n):
        if j in visited[i]:
            row.append("1")
        else:
            row.append("0")
    print(" ".join(row))