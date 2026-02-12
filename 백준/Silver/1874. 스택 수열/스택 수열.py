import sys
input = sys.stdin.readline

n = int(input())
stacks = []
result = []
count = 1
possilbe = True

for _ in range(n):
    target = int(input())
    
    while target >= count:
        stacks.append(count)
        count += 1
        result.append("+")
        
    if stacks and stacks[-1] == target:
        stacks.pop()
        result.append("-")
    else:
        possilbe = False
        break

if possilbe:
    print('\n'.join(result))
else:
    print("NO")        