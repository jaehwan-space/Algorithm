def solution(numLog):
    answer = ''
    path = {1 : 'w', -1 : 's', 10 : 'd', -10 : 'a'}
    
    for i in range(len(numLog) - 1):
        answer += path[numLog[i + 1] - numLog[i]]
    return answer