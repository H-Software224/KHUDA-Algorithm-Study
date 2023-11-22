#숫자 찾기
def solution(num, k):
    return str(num).index(str(k)) + 1 if str(k) in str(num) else -1

#n의 배수 고르기
def solution(n, numlist):
    return [i for i in numlist if i%n == 0]

#자릿수 더하기
def solution(n):
    return sum(int(i) for i in str(n))

#ox퀴즈
def solution(quiz):
    for i in range (len(quiz)):
        array = quiz[i].split('=')
        answer = array[1].strip()
        real_answer = str(eval(array[0])).strip()
 
        if answer == real_answer:
            quiz[i] = "O"
        else:
            quiz[i] = "X"
    return quiz