def solution(code):
    mode = 0
    ret = ''
    for i in range(len(code)):
        if code[i] == '1':
            mode = int(not mode)
            continue
        
        if mode == 0:
            if i % 2 == 0:
                ret += code[i]
        else:
            if i % 2 == 1:
                ret += code[i]
    return ret if len(ret) > 0 else "EMPTY"