import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nli = set([input().rstrip() for _ in range(n)])
mli = set([input().rstrip() for _ in range(m)])

result = sorted(list(nli & mli))
print(len(result))
for i in result:
    print(i)