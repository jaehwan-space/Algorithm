pos = input().strip()

# 열(a~h) → 숫자(1~8)
x = ord(pos[0]) - ord('a') + 1
y = int(pos[1])

# 나이트 이동 방향 (8가지)
moves = [
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2),  (1, 2),
    (2, -1),  (2, 1)
]

count = 0

for dx, dy in moves:
    nx = x + dx
    ny = y + dy
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)
