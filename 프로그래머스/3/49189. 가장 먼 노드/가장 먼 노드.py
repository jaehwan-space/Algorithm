import heapq
INF = int(1e9)

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    
    for a, b in edge:
        graph[a].append((b, 1))
        graph[b].append((a, 1))
    
    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, node = heapq.heappop(q)
            if distance[node] > dist:
                continue
            for i in graph[node]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra(1)
    distance[0] = 0
    
    answer = 0
    for i in distance:
        if i == max(distance):
            answer += 1
            
    return answer