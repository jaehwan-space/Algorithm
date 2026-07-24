import math

def solution(num_list):
    if len(num_list) > 10:
        return sum(num_list)
    else:
        return math.prod(num_list)