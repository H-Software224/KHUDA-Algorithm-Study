#컨트롤 제트
def solution(s):
    split_list = s.split()
    for i in range (1,len(split_list)):
        if split_list[i] == 'Z' :
            split_list[i-1] = 0
            split_list[i] = 0
    sum = 0
    for num in split_list:
        sum += int(num)

    return sum

#배열 원소의 길이
def solution(strlist):
    answer = []
    for str in strlist:
        answer.append(len(str))
    
    return answer

#중복된 문자 제거
def solution(my_string):
    answer = ''
    for char in my_string:
        if char not in answer:
            answer += char
    return answer

#삼각형의 완성 조건
def solution(sides):
    sides.sort(reverse = True)
    return 1 if sides[0] < sides[1] + sides[2] else 2

