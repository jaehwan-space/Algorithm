k = int(input())
stacks = []

for _ in range(k):
    n = int(input())
    if n == 0:
        stacks.pop()
    else:
        stacks.append(n)

print(sum(stacks))