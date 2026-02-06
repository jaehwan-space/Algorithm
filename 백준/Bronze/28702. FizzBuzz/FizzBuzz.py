def fizzbuzzgame(i):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

strings = [input().strip() for _ in range(3)]

for i in range(3):
    if strings[i].isdigit():
        fizzbuzzgame(int(strings[i]) + 3 - i)
        break