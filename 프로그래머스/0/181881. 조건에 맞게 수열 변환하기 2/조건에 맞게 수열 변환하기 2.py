def solution(arr):
    count = 0
    while True:
        prev = arr.copy()
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i] // 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i] * 2 + 1
        count += 1
        if prev == arr:
            return count - 1
    return count