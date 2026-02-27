import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def turn_dir():
    global d
    d -= 1
    if d == -1:
        d = 3
        
while True:
    if graph[r][c] == 0:
        graph[r][c] = 2
        result += 1
    turnc = 0
    for i in range(4):
        turn_dir()
        nx = c + dx[d]
        ny = r + dy[d]
        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
            c = nx
            r = ny
            break
        else:
            turnc += 1
    if turnc == 4:
        nx = c - dx[d]
        ny = r - dy[d]
        if graph[ny][nx] == 1:
            print(result)
            exit()
        else:
            c = nx
            r = ny
print(result)