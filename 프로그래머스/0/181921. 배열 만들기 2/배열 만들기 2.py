def solution(l, r):
    answer = []
    
    for i in range(l, r + 1):
        passed = True
        for j in str(i):
            if j != '0' and j != '5':
                passed = False
                break
        if passed:
            answer.append(i)
        
    return answer if len(answer) != 0 else [-1]