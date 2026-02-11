n = int(input())

lists = []

for _ in range(n):
    x, y = map(int, input().split())
    lists.append([x, y])
    
lists.sort(key=lambda x:(x[0], x[1]))
for i in lists:
    print(*i)