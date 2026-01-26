n, m = map(int, input().split())
x, y, dir = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
visited = [[0] * m for _ in range(n)]

visited[x][y] = 1
count = 1

def turn_left():
    global dir
    dir -= 1
    if dir == -1:
         dir = 3

while True:
    check = 0
    for i in range(4):
        turn_left()
        nx = x + dx[dir]
        ny = y + dy[dir]
        if visited[nx][ny] == 1 or maps[nx][ny] == 1:
            check += 1
            continue
        x, y = nx, ny
        visited[x][y] = 1
        count += 1
        break
    if check == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        if maps[nx][ny] == 0:
            x, y = nx, ny
            check = 0
        else:
            break
        
print(count)