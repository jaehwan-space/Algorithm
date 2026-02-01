n = int(input())
result = 0

start = max(0, n - 9 * len(str(n)))

for m in range(start, n):
    s = m + sum(map(int, str(m)))
    if s == n:
        result = m
        break

print(result)
