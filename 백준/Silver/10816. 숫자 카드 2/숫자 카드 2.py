from bisect import bisect_left, bisect_right

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
cards.sort()
    
for i in list(map(int, input().split())):
    print(bisect_right(cards, i) - bisect_left(cards, i), end=" ")