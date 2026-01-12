print('hi')    
n, m = map(int, input().split())
cards = []
min = 0

for _ in range(n):
    cards.append(list(map(int, input().split())))
 
for card_list in cards:
    card_list.sort()
    if card_list[0] > min:
        min = card_list[0]
print(min)