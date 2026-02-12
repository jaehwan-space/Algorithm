n, m = map(int, input().split())
board = [input() for _ in range(n)]

min_count = 64 

for x in range(n - 7):
    for y in range(m - 7):

        count_w = 0  # 왼쪽 위가 W일 때
        count_b = 0  # 왼쪽 위가 B일 때

        for i in range(8):
            for j in range(8):

                current = board[x+i][y+j]

                if (i + j) % 2 == 0:
                    if current != 'W':
                        count_w += 1
                    if current != 'B':
                        count_b += 1
                else:
                    if current != 'B':
                        count_w += 1
                    if current != 'W':
                        count_b += 1

        min_count = min(min_count, count_w, count_b)

print(min_count)
