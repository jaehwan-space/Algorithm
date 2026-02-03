def binary(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary(array, target, start, mid - 1)
    else:
        return binary(array, target, mid + 1, end)

n = int(input())
shop = list(map(int, input().split()))
shop.sort()
m = int(input())
customer = list(map(int, input().split()))
result = []

for i in customer:
    if binary(shop, i, 0, n) == None:
        result.append("no")
    else:
        result.append("yes")

print(*result)