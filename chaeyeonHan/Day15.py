#영어가 싫어요
def solution(numbers):
    dict = {"zero" : '0', "one":'1', "two":'2',"three" : '3', "four":'4', "five":'5',"six" : '6', "seven": '7', "eight" : '8', "nine" : '9'}
    for key in dict:
        if key in numbers:
            numbers = numbers.replace(key,dict[key])
   
    return int(numbers)

#인덱스 바꾸기
def solution(my_string, num1, num2):
    answer = my_string[:num1]+my_string[num2] + my_string[num1 + 1 : num2] + my_string[num1] + my_string[num2+1:]
    return answer

#한 번만 등장한 문자
def solution(s):
    once_list = []
    for char in set(s):
        if s.count(char) == 1:
            once_list.append(char)
    answer = ''.join(sorted(once_list))
    return answer

#약수 구하기
def solution(n):
    answer = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            answer.extend([i,n//i])
    return sorted(answer)