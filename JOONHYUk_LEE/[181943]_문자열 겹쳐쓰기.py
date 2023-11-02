def solution(my_string, overwrite_string, s):
    
    # s = my_string의 변환 index값 
    # overwrite_string = 바뀔 문자열.(해당 길이만큼 바뀌고, 뒤에 나머지는 유지)

    my_string = list(my_string)
    
    for i in range(len(overwrite_string)):
        my_string[s + i] = overwrite_string[i]
    
    result = ''.join(my_string)
    return result