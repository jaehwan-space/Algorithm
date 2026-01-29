n = int(input())

for _ in range(n):
    texts = input()
    print(texts[0], texts[len(texts)-1], sep="")