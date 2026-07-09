def solution(arr, queries):
    result = []
    for s, e, k in queries:
        a = []
        for i in arr[s:e+1]:
            if k < i:
                a.append(i)
        result.append(-1 if len(a) == 0 else min(a))
    return result