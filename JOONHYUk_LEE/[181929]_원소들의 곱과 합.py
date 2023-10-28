def solution(num_list):
    num_sum = 0
    num_multi = 1
    for i in num_list:
        num_multi *= i
        num_sum += i
        
    if num_multi < num_sum ** 2:
        return 1
    else:
        return 0