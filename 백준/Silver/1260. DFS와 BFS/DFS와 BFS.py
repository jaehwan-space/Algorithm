import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, v = map(int, input().split()) 

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
dfs_g = []
bfs_g = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(arr, visit, start):
    visit[start] = True
    dfs_g.append(start)
    arr[start].sort()
    for i in arr[start]:
        if not visit[i]:
            dfs(arr, visit, i)

def bfs(arr, visit, start):
    q = deque(arr[start])
    # dfs 이미 정렬됨
    bfs_g.append(start)
    visit[start] = True
    while q:
        node = q.popleft()
        if not visit[node]:
            visit[node] = True
            bfs_g.append(node)
            q.extend(arr[node])
    
dfs(graph, visited, v)
visited = [False] * (n + 1)
bfs(graph, visited, v)
print(*dfs_g)
print(*bfs_g)