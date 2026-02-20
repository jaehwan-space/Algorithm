import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
grid = [list(input().strip()) for _ in range(N)]

visited = [[False]*N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, color):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and grid[nx][ny] == color:
                dfs(nx, ny, color)

normal = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, grid[i][j])
            normal += 1

for i in range(N):
    for j in range(N):
        if grid[i][j] == 'R':
            grid[i][j] = 'G'

visited = [[False]*N for _ in range(N)]

color_blind = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, grid[i][j])
            color_blind += 1

print(normal, color_blind)