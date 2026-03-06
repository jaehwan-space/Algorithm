from collections import deque

def solution(maps):
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    def bfs(x, y):
        q = deque()
        q.append((x,y))
        while q:
            a, b = q.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps):
                    if maps[ny][nx] == 1:
                        q.append((nx, ny))
                        maps[ny][nx] = maps[b][a] + 1
    bfs(0, 0)
    if maps[len(maps) - 1][len(maps[0]) - 1] == 1:
        return -1
    else:
        return maps[len(maps) - 1][len(maps[0]) - 1]