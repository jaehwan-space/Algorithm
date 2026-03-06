def solution(n, computers):
    graph = [[] for _ in range(n)]
    visited = [False] * n
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)

    def dfs(num):
        if not visited[num]:
            visited[num] = True
            for i in graph[num]:                          
                dfs(i)
            return True
        return False
    
    answer = 0
    for i in range(len(computers)):
        if dfs(i) == True:
            answer += 1

    return answer