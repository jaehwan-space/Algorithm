def solution(a, b):
    a = str(a)
    b = str(b)
    
    if int(a + b) > int(b + a):
        return int(a + b)
    else:
        return int(b + a)