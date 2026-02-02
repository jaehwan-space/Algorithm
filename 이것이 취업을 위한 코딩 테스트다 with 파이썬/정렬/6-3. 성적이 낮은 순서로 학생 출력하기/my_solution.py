n = int(input())

scores = {}

for _ in range(n):
    name, score = input().split()
    scores[name] = int(score)

print(*sorted(scores, key=lambda x: scores[x]))
