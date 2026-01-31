n = int(input())

for _ in range(n):
    count = 0
    lists = input().split("X")
    for i in lists:
        count += len(i) * (len(i) + 1) // 2
    print(count)