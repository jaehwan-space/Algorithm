def solution(my_string, indices):
    indices.sort()
    my_string = list(my_string)
    for i in indices[::-1]:
        my_string.pop(i)
    return ''.join(my_string)