def solution(my_string):
    answer = []
    for i in range(65, 91):
        answer.append(my_string.count(chr(i)))
    for i in range(97, 123):
        answer.append(my_string.count(chr(i)))
    return answer