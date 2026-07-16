def solution(arr):
    answer = []
    indexs = list(filter(lambda x: arr[x] == 2, range(len(arr))))
    return arr[indexs[0]:indexs[-1] + 1] if not len(indexs) == 0 else [-1]