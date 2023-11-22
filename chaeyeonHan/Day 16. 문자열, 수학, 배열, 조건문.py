
#편지
def solution(message):
    return len(message) * 2

#가장 큰 수 찾기
def solution(array):
    
    answer = [max(array), array.index(max(array))]
    return answer

#문자열 계산하기
def solution(my_string):
    return eval(my_string)

#배열의 유사도
def solution(s1, s2):
    answer = 0
    for elem in s1: 
        if elem in s2:
            answer += 1
    return answer