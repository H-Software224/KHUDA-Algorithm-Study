# 181907 문자열의 앞의 n글자
def solution(my_string, n):

    return my_string[:n]

# 181906 접두사인지 확인하기
def solution(my_string, is_prefix):
    answer = 0
    list1 = []
    for i in range(len(my_string)):
        list1.append(my_string[:i])
    if is_prefix in list1:
        return 1
    return 0

# 181905 문자열 뒤집기
def solution(my_string, s, e):
    answer = ''
    return my_string[:s] + my_string[s:e + 1][::-1] + my_string[e+1:]

# 181904 세로 읽기
def solution(my_string, m, c):
    list1 = []
    for i in range(c-1, len(my_string), m):
        list1.append(my_string[i])
    return ''.join(list1)
"""
return my_string[c-1::m]
"""

# 181903 qr code
def solution(q, r, code):
    answer = ''
    list1 = []
    for i in range(len(code)):
        if i % q == r:
            list1.append(code[i])
    answer = ''.join(list1)
    return answer