n = int(input())
lists = input()
r = 31
result = 0

def stringtoint(str):
    return ord(str) - 96

for i in range(len(lists)):
    result += stringtoint(lists[i]) * (r ** i)
    
print(result)