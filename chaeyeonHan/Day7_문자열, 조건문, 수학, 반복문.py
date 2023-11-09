#특정 문자 제거하기
def solution(my_string, letter):
    answer = ''
    for char in my_string:
        if char != letter:
            answer += char
    return answer

#각도기
def solution(angle):
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    elif angle == 180:
        return 4
    
#양꼬치
def solution(n, k):
    sum = 12000 * n + 2000 *(k- n//10)
    return sum

#짝수의 합
def solution(n):
    sum = 0
    for i in range(0,n+1,2):
        sum += i
    return sum