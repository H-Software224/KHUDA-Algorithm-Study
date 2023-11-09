#가까운 수
def solution(array, n):
    abs_list = [abs(n-i) for i in array]
    min_list = []
    min_idx = [index for index, value in enumerate(abs_list) if value == min(abs_list)]
    if len(min_idx) >= 2:
        return min(array[i] for i in min_idx)
            
    return array[min_idx[0]]

#369게임
def solution(order):
    count = 0
    for num in str(order):
        if num in '369':
            count += 1
    return count

#암호 해독
def solution(cipher, code):
    answer = ''
    for i in range (1, len(cipher)//code + 1):
        answer += cipher[code * i - 1]
    return answer

#대문자와 소문자
def solution(my_string):
    new_string = ''
    for char in my_string:
        if char.isupper():
            new_string += char.lower()
        else:
            new_string += char.upper()
    return new_string
