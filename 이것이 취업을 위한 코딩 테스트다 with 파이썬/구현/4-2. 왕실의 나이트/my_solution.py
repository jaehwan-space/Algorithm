loc = input()

row = "abcdefgh"
x, y = row.index(loc[0]) + 1, int(loc[1])

dx = [2, 2, -2, -2, -1, 1, 1, -1]
dy = [-1, 1, -1, 1, 2, 2, -2, -2]
count = 0

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    if not(nx < 1 or ny < 1 or nx > 8 or ny > 8):
        count += 1

print(count)