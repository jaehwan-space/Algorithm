n = int(input())
plans = input().split()

# 방향 매핑
move = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

y, x = 1, 1

for p in plans:
    dy, dx = move[p]
    ny, nx = y + dy, x + dx

    if 1 <= ny <= n and 1 <= nx <= n:
        y, x = ny, nx

print(y, x)
