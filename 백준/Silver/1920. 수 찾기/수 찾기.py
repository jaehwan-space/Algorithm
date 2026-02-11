import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())

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

for i in list(map(int, input().split())):
    if binary(a, i, 0, n - 1) == None:
        print(0)
    else:
        print(1)