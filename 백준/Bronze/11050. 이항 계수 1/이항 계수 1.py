def factorial(a):
    if a <= 1:
        return 1
    return a * (factorial(a - 1))

n, k = map(int, input().split())
print(int(factorial(n) / (factorial(k) * factorial(n - k))))