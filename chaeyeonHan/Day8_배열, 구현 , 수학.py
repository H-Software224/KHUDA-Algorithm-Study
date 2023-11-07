#배열 자르기
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

#외계행성의 나이
def solution(age):
    answer = ''
    age = str(age)
    for i in range (len(age)):
        answer += chr(int(str(age)[i]) + 97)
    return answer

#진료순서 정하기
def solution(emergency):
    sorted_list = sorted(emergency,reverse = True)
    for i in range(len(emergency)):
        emergency[i] = sorted_list.index(emergency[i])+1
    return emergency

#순서쌍의 개수
def solution(n):
    count = 0
    for i in range (1,n+1):
        if n % i == 0:
            count += 1
    return count