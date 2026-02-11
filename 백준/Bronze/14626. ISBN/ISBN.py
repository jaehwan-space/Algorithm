isbn = input()

star_idx = isbn.index('*')
total = 0

for i in range(13):
    if i == star_idx:
        continue
    num = int(isbn[i])
    if i % 2 == 0:
        total += num
    else:
        total += num * 3

for x in range(10):
    if star_idx % 2 == 0:
        temp = total + x
    else:
        temp = total + x * 3

    if temp % 10 == 0:
        print(x)
        break
