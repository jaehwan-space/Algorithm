from collections import deque
m, n = map(int, input().split())
box = []
queue = deque()
dx = [0, 1, 0 , -1]
dy = [-1, 0, 1, 0]

for _ in range(n):
    box.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((j, i))
            
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if box[ny][nx] == 0:
                queue.append((nx, ny))
                box[ny][nx] = box[y][x] + 1
            
answer = 0
for row in box:
    for v in row:
        if v == 0:
            print("-1")
            exit()
        answer = max(answer, v)

print(answer - 1)