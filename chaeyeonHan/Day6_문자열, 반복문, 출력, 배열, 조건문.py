#문자열 뒤집기

def solution(my_string):
    rev_string = ''
    for i in range(len(my_string)):
        rev_string = rev_string + my_string[-1-i]
        
    
    return  rev_string

#직각삼각형 출력하기
n = int(input())
for i in range (n):
    print('*' * (i+1))

#짝수 홀수 개수

def solution(num_list):
    odd = 0
    even = 0
    for num in num_list:
        if num %2 ==0:
            even += 1
        else:
            odd += 1
    answer = [even,odd]
    return answer

#문자 반복 출력하기
def solution(my_string, n):
    answer = ''
    for char in my_string:
        answer = answer + char * n
    return answer