def solution(n, results):
    graph = [[False]*(n+1) for _ in range(n+1)]

    for a, b in results:
        graph[a][b] = True

    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                if graph[a][k] and graph[k][b]:
                    graph[a][b] = True

    answer = 0

    for i in range(1, n+1):
        win = 0
        lose = 0

        for j in range(1, n+1):
            if graph[i][j]:
                win += 1
            if graph[j][i]:
                lose += 1

        if win + lose == n-1:
            answer += 1

    return answer