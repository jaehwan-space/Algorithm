def binary(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    result = sum([n - mid for n in array if n - mid > 0])
    if result == target:
        return mid
    elif result < target:
        return binary(array, target, start, mid - 1)
    else:
        return binary(array, target, mid + 1, end)

n, m = map(int, input().split())
he = list(map(int, input().split()))

print(f"정답: {binary(he, m, 0, max(he))}")