tasks = []
n = []
for _ in range(28):
    tasks.append(int(input()))

for i in range(1, 31):
    if not i in tasks:
        n.append(i)
        
print(*n, sep='\n')