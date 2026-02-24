import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

dx = [
    [0,0,0,0], [0,1,2,3],          # ㅡ
    [0,0,1,1],                    # 네모
    [0,1,2,2], [0,1,2,2],         # L
    [0,0,1,2], [0,0,1,2],
    [0,1,1,1], [0,1,1,1],
    [0,0,0,1], [0,0,0,1],
    [0,0,1,1], [0,1,1,2],         # S
    [0,0,1,1], [0,1,1,2],
    [0,0,0,1], [0,1,1,2],         # ㅗ
    [1,1,1,0], [0,1,2,1]
]

dy = [
    [0,1,2,3], [0,0,0,0],          # ㅡ
    [0,1,0,1],                    # 네모
    [0,0,0,1], [1,1,1,0],         # L
    [0,1,0,0], [0,1,1,1],
    [0,0,1,2], [2,0,1,2],
    [0,1,2,0], [0,1,2,2],
    [0,1,1,2], [1,0,1,0],         # S
    [1,2,0,1], [0,0,1,1],
    [0,1,2,1], [1,0,1,1],         # ㅗ
    [0,1,2,1], [0,0,0,1]
]

for i in range(n):
    for j in range(m):
        for shape in range(19):
            total = 0
            valid = True
            for k in range(4):
                nx = i + dx[shape][k]
                ny = j + dy[shape][k]

                if 0 <= nx < n and 0 <= ny < m:
                    total += board[nx][ny]
                else:
                    valid = False
                    break

            if valid:
                answer = max(answer, total)
                
print(answer)