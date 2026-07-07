def solution(n):
    answer = 0
    if n % 2 == 1 :
        for i in range(n, 0, -2):
            answer += i
    else:
        for i in range(n, 0, -2):
            answer += i ** 2
    return answer