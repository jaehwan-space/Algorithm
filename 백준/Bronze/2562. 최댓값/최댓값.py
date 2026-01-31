lists = []
for _ in range(9):
    lists.append(int(input()))

print(max(lists))
print(lists.index(max(lists)) + 1)
