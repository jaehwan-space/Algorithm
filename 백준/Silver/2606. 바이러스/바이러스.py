import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

com = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    com[a].append(b)
    com[b].append(a)
    
def dfs(arr, v, t):
    v[t] = True
    for i in arr[t]:
        if not v[i]:
            dfs(arr, v, i)
            
dfs(com, visited, 1)
print(visited.count(True) - 1)