def solution(n, control):
    path = {'w' : 1, 's' : -1, 'd' : 10, 'a' : -10}
    for i in control:
        n += path[i]
    return n