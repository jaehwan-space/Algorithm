n = int(input())
plans = list(input().split())

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']
loc = [1, 1]

def changePlan(a):
    return move.index(a)

plans = list(map(changePlan, plans))

for i in plans:
    ny = loc[0] + dy[i]
    nx = loc[1] + dx[i]
    if ny < 1 or nx < 1 or ny > n or nx > n:
        continue
    loc[0], loc[1] = ny, nx

print(*loc, sep=' ')