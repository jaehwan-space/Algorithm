n = input().strip()
result = 0.0

if n == "F":
    result = 0.0
else:
    if n[0] == "A":
        result = 4.0
    elif n[0] == "B":
        result = 3.0
    elif n[0] == "C":
        result = 2.0
    elif n[0] == "D":
        result = 1.0

    # 보정
    if n[1] == "+":
        result += 0.3
    elif n[1] == "-":
        result -= 0.3

print(result)
