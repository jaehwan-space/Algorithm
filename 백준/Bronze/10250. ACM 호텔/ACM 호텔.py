n = int(input())
for _ in range(n):
    h, w, n = map(int, input().split())
    x = n // h # 호수
    if n % h == 0:
        y = h # 층수
    else:
        y = n % h
        x += 1
    print(y, format(x, "02"), sep="")