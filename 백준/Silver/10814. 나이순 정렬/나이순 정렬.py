n = int(input())
people = []
count = 0
for _ in range(n): 
    age, name = input().split()
    people.append([int(age), name, count])
    count += 1

people.sort(key=lambda x: (x[0], x[2]))
for age, name, _ in people:
    print(age, name)