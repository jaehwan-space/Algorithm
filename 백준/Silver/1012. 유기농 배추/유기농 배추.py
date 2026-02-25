import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

def dfs(graph, loc):
    x, y = loc
    if 0 <= x < len(graph[0]) and 0 <= y < len(graph) and graph[y][x] == 1:
        graph[y][x] = 0
        dfs(graph, (x - 1, y))
        dfs(graph, (x + 1, y))
        dfs(graph, (x, y - 1))
        dfs(graph, (x, y + 1))
    

for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1
    
    result = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                dfs(board, (j, i))
                result += 1
                
    print(result)