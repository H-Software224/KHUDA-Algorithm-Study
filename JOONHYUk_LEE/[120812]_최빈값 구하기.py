def solution(array):
    dic = {}
    for item in array:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
    max_count = max(dic.values())
    max_elements = [key for key, value in dic.items() if value == max_count]
    if len(dic) == 1:
        return array[0]    
    elif len(max_elements) == 1:
        return max_elements[0]
    else:
        return -1