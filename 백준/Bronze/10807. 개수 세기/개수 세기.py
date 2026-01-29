n = int(input())
m = list(map(int, input().split()))
x = int(input())

result = 0

for i in m:
    if x == i:
        result += 1

print(result)