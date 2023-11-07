# 181912 <배열 만들기 5>
def solution(intStrs, k, s, l):
    answer = []
    for i in range(len(intStrs)):
        ch = int(intStrs[i][s:s + l])        
        if ch > k:answer.append(ch)
    return answer

# 181911 <부분 문자열 이어 붙여 문자열 만들기>
def solution(my_strings, parts):
    answer = ''
    
    for i in range(len(my_strings)):
        s, e = parts[i][0], parts[i][1]
        part_ch = my_strings[i][s:e + 1]
        answer += ''.join(part_ch)      
    return answer

# 181910 <문자열의 뒤의 n글자>
def solution(my_string, n):
    answer = ''
    length = len(my_string)
    answer = my_string[- n:]
    return answer

# 181909 <접미사 배열>
def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i:])
    
    return sorted(answer)

# 181908 <접미사인지 확인하기>
def solution(my_string, is_suffix):
    answer = 0
    list1 = []
    for i in range(len(my_string)):
        list1.append(my_string[i:])
    
    if is_suffix in list1:
        return 1
    else:
        return 0



