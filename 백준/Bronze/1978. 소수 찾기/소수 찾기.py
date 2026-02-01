_ = int(input())

def is_prime(m):
    if m < 2:
        return False
    for i in range(2, int(m ** 0.5) + 1):
        if m % i == 0:
            return False
    return True

lists = list(map(int, input().split()))
print(len([m for m in lists if is_prime(m)]))