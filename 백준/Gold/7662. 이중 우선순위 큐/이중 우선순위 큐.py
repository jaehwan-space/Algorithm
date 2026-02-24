import sys
import heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    
    minq = []
    maxq = []
    visited = [False] * k
    
    for i in range(k):
        ty, num = input().split()
        num = int(num)
        
        if ty == "I":
            heapq.heappush(minq, (num, i))
            heapq.heappush(maxq, (-num, i))
            visited[i] = True
        elif ty == "D":
            if num == 1:
                while maxq and not visited[maxq[0][1]]:
                    heapq.heappop(maxq)
                if maxq:
                    visited[maxq[0][1]] = False
                    heapq.heappop(maxq)
            elif num == -1:
                while minq and not visited[minq[0][1]]:
                    heapq.heappop(minq)
                if minq:
                    visited[minq[0][1]] = False
                    heapq.heappop(minq)
                    
    while maxq and not visited[maxq[0][1]]:
        heapq.heappop(maxq)
    while minq and not visited[minq[0][1]]:
        heapq.heappop(minq)
        
    if not minq or not maxq:
        print("EMPTY")
    else:
        print(-maxq[0][0], minq[0][0])