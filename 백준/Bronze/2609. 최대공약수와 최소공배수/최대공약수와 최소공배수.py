n, m = map(int, input().split())

def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_lcm(a, b):
    return (a * b) // get_gcd(a, b)

print(get_gcd(n, m))
print(get_lcm(n, m))