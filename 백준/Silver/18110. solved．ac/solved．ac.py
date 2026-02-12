import sys
input = sys.stdin.readline

n = int(input())
if n != 0:
    scores = sorted([int(input()) for _ in range(n)])
    ex = int(n * 0.15 + 0.5)
    scores = scores[ex:n-ex]
    print(int(sum(scores) / len(scores) + 0.5))
else:
    print(0)