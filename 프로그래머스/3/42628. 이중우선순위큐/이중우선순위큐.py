import heapq

def solution(operations):
    maxq = []
    minq = []
    visited = [False] * (len(operations) + 1)
    
    for i in range(len(operations)):
        t, num = operations[i].split()
        num = int(num)
        
        if t == "I":
            heapq.heappush(maxq, (-num, i))
            heapq.heappush(minq, (num, i))
            visited[i] = True
        elif t == "D":
            if num == 1:
                while maxq and not visited[maxq[0][1]]:
                    heapq.heappop(maxq)
                
                if maxq:
                    visited[maxq[0][1]] = False
                    heapq.heappop(maxq)
            if num == -1:
                while minq and not visited[minq[0][1]]:
                    heapq.heappop(minq)
                
                if minq:
                    visited[minq[0][1]] = False
                    heapq.heappop(minq)
                    
    while maxq and not visited[maxq[0][1]]:
        heapq.heappop(maxq)                
    while minq and not visited[minq[0][1]]:
        heapq.heappop(minq)
            
    if maxq and minq:      
        answer = [-maxq[0][0], minq[0][0]]
    else:
        answer = [0, 0]
    return answer