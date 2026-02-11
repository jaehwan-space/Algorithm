t = int(input())

for _ in range(t):
    k, n = int(input()), int(input())
    maps = [[0] * n for _ in range(k+1)]  

    for i in range(k+1):
        for j in range(n):
            if i == 0:
                maps[i][j] = j + 1
            elif j == 0:
                maps[i][j] = maps[i-1][j]
            else:
                maps[i][j] = maps[i][j-1] + maps[i-1][j]
    print(maps[k][n-1])
    