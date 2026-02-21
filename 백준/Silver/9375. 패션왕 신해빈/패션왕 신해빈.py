import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    clothes = {}
    for _ in range(n):
        name, kind = map(str, input().split())
        if not kind in clothes.keys():
            clothes[kind] = []
        clothes[kind].append(name)
    result = 1
    for i in clothes:
        result *= len(clothes[i]) + 1
    print(result - 1)
    