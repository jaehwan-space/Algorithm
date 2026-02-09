n = int(input())
lengths = [["0"] for _ in range(51)]
words = []
for _ in range(n):
    words.append(input())
    
words = set(words)
words = list(words)

for word in words:
    lengths[len(word)].append(word)

for i in range(len(lengths)):
    lengths[i].sort()
    
for i in lengths:
    if len(i) <= 1:
        continue
    for j in range(1, len(i)):
        print(i[j])