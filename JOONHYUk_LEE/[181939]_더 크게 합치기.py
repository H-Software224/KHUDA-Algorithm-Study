def solution(a, b):
    return max(int(f'{a}{b}'), int(f'{b}{a}'))
    """
    answer = 0
    temp1 = int(str(a) + str(b))
    temp2 = int(str(b) + str(a))
    
    if temp1 > temp2:
        return temp1
    else:
        return temp2
    """