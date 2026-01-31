from collections import deque

n, m = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

count = 0
maps = []
for _ in range(n):
    maps.append(list(map(int, input())))

def bfs():
    global count
    queue = deque([[0, 0]])
    maps[0][0] = 0
    while queue:
        [x, y] = queue.popleft()
        if x+1 == n and y+1 == m:
            break
        count += 1
        ck = 0
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny <0 or nx >= n or ny >= m:
                continue
            if maps[nx][ny] == 1:
                queue.append([nx, ny])
            else:
                ck += 1
        if ck == 4:
            count -= 1
    print(count)

bfs()