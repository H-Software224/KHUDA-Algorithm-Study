#모음 제거
def solution(my_string):
    my_string = ''.join(char for char in my_string if char not in ['a','e','i','o','u'])
    return my_string

#문자열 정렬하기(1)
def solution(my_string):
    numlist = [int(x) for x in my_string if x.isdigit()]
    return sorted(numlist)

#숨어있는 숫자의 덧셈(1)
def solution(my_string):
    numlist = [int(x) for x in my_string if x.isdigit()]
    return sum(numlist)

#소인수분해
def solution(n):
    prime_list = [i for i in range (2,n+1)]
    j = 0
    while len(prime_list) > j:
        for num in prime_list[j+1:]:
            if num % prime_list[j] == 0:
                prime_list.remove(num)
        j += 1

    answer = []         
    while n >1:
        for num in prime_list:
            if n % num  == 0:
                answer.append(num)
                n = n // num
    return sorted(list(set(answer)))
        
                