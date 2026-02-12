n = int(input())
for _ in range(n):
    st = input()
    count = 0
    for i in st:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            count = -1
            break
    if count == 0:
        print("YES")
    else:
        print("NO")