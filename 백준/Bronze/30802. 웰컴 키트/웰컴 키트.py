import math

n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())

tt = 0
for i in sizes:
    tt += math.ceil(i / t)

print(tt)
print(n // p, n % p)