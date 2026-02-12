import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
lists = sorted([int(input()) for _ in range(n)])

print(round(sum(lists) / n))
print(lists[n // 2])
mc = Counter(lists).most_common(2)
if len(mc) > 1 and mc[0][1] == mc[1][1]:
    print(mc[1][0])
else:
    print(mc[0][0])
print(max(lists) - min(lists))