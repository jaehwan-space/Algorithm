n = int(input())
s = input()

r = 31
m = 1234567891
result = 0

def stringtoint(c):
    return ord(c) - 96  # a=1

for i in range(len(s)):
    result = (result + stringtoint(s[i]) * (r ** i)) % m

print(result)
