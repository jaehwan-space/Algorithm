import sys
input = sys.stdin.readline

lists = []
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    lists.append((a, b))
lists.sort(key=lambda x:(x[1], x[0]))

count = 0
end_time = 0

for start, end in lists:
    if start >= end_time:
        count += 1
        end_time = end

print(count)