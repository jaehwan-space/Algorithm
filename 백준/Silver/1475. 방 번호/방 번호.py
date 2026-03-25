import sys
import math
input = sys.stdin.readline

n = input().strip()
answer = [0] * 9

for i in range(len(n)):
    target = int(n[i])
    if target == 9:
        target = 6
    answer[target] += 1
    
answer[6] = math.ceil(answer[6] / 2)
print(max(answer))   