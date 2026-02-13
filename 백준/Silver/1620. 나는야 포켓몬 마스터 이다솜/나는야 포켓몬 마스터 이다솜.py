import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lists = []
dic = {}
for i in range(n):
    txt = input().rstrip()
    lists.append(txt)
    dic[txt] = i



for _ in range(m):
    txt = input().rstrip()
    if txt.isdigit():
        print(lists[int(txt) - 1])
    else:
        print(dic[txt] + 1)