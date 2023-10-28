def solution(num_list):
    num_even = ''
    num_odd = ''
    for i in num_list:
        if i % 2 == 0:
            num_even += ''.join(str(i))
        else:
            num_odd += ''.join(str(i))
            
    return int(num_even) + int(num_odd)