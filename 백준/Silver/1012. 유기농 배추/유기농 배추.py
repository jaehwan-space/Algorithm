import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)

for _ in range(T):
    M, N, K = map(int, input().split())
    
    board = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1  
    
    count = 0
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1
                
    print(count)