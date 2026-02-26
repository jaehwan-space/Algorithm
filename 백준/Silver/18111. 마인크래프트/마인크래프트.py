import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())

height_count = [0] * 257
min_h = 256
max_h = 0

for _ in range(n):
    row = list(map(int, input().split()))
    for h in row:
        height_count[h] += 1
        min_h = min(min_h, h)
        max_h = max(max_h, h)

sec = float('inf')
answer_height = 0

for target in range(min_h, max_h + 1):
    remove = 0
    add = 0
    
    for h in range(min_h, max_h + 1):
        if h > target:
            remove += (h - target) * height_count[h]
        else:
            add += (target - h) * height_count[h]
    
    if remove + b >= add:
        time = remove * 2 + add
        
        if time < sec or (time == sec and target > answer_height):
            sec = time
            answer_height = target

print(sec, answer_height)