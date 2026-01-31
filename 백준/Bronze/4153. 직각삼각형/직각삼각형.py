while True:
    lines = list(map(int, input().split()))
    lines.sort()
    a, b, c = lines
    if a == 0:
        break
    if a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")