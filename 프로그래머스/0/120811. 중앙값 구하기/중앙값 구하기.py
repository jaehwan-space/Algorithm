import math

def solution(array):
    array.sort()
    
    return array[math.ceil(len(array)/2) - 1]