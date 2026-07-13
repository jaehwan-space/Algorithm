from collections import Counter

def solution(a, b, c, d):
    dice = [a, b, c, d]
    counter = Counter(dice)

    # [(숫자, 개수), ...]
    items = list(counter.items())

    # 4개 모두 같은 경우
    if len(items) == 1:
        return 1111 * items[0][0]

    # 3+1 또는 2+2
    if len(items) == 2:
        (n1, c1), (n2, c2) = items

        # 3+1
        if c1 == 3 or c2 == 3:
            if c1 == 3:
                p, q = n1, n2
            else:
                p, q = n2, n1
            return (10 * p + q) ** 2

        # 2+2
        return (n1 + n2) * abs(n1 - n2)

    # 2+1+1
    if len(items) == 3:
        others = []
        for num, cnt in items:
            if cnt == 1:
                others.append(num)
        return others[0] * others[1]

    # 1+1+1+1
    return min(dice)