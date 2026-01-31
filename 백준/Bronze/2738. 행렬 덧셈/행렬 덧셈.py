n, m = map(int, input().split())
a, b = [], []
result = [[0]*m for _ in range(n)]

for _ in range(n):
    a.append(list(map(int, input().split())))
for _ in range(n):
    b.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(m):
        result[i][j] = a[i][j] + b[i][j]
        
for i in result:
    print(*i)