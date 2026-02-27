import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
mv_plan = list(map(int, input().split()))
# 윗면 서 북 남 동 아랫면
dice = [0, 0, 0, 0, 0, 0]

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def roll_dice(direction):
    temp = dice.copy()
    if direction == 1:
        dice[0] = temp[4]
        dice[1] = temp[0]
        dice[4] = temp[5]
        dice[5] = temp[1]
    elif direction == 2:
        dice[0] = temp[1]
        dice[1] = temp[5]
        dice[4] = temp[0]
        dice[5] = temp[4]
    elif direction == 3:
        dice[0] = temp[3]
        dice[5] = temp[2]
        dice[2] = temp[0]
        dice[3] = temp[5]
    else:
        dice[0] = temp[2]
        dice[5] = temp[3]
        dice[2] = temp[5]
        dice[3] = temp[0]

for i in mv_plan:
    ny = y + dy[i - 1]
    nx = x + dx[i - 1]
    if not (0 <= ny < m and 0 <= nx < n):
        continue
    roll_dice(i)
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[5]
    else:
        dice[5] = graph[nx][ny]
        graph[nx][ny] = 0
    print(dice[0])
    y = ny
    x = nx
    