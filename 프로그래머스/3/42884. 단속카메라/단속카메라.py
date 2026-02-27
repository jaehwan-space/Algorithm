def solution(routes):
    answer = [30001]
    routes.sort(key=lambda x:(x[1], x[0]))
    for start, end in routes:
        if start <= answer[-1] <= end:
            continue
        else:
            answer.append(end)
    return (len(answer) - 1)