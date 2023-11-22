#문자열안에 문자열
def solution(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2
    
#제곱수 판별하기
def solution(n):
    answer = 2
    for i in range (1,int(n**0.5)+1):
        if n / i == i:
            answer = 1
    return answer

#세균 증식
def solution(n, t):
    return n * (2**t)

#문자열 정렬하기(2)
def solution(my_string):
    return ''.join(sorted(my_string.lower()))