def solution(num_list):
    last_num = num_list[-1]
    sec_num = num_list[-2]
    if last_num > sec_num:
        num_list.append(last_num - sec_num)
    else:
        num_list.append(last_num * 2)
    return num_list