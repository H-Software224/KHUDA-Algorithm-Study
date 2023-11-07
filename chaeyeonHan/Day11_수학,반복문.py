#주사위의 개수
def solution(box, n):
    return (box[0]//n) * (box[1]//n) * (box[2]//n)

#합성수 찾기
def solution(n):
    prime_list = [i for i in range (2,n+1)]
    j = 0
    while len(prime_list) > j:
        for num in prime_list[j+1:]:
            if num % prime_list[j] == 0:
                prime_list.remove(num)
        j += 1
        
    return n - len(prime_list) - 1

#최댓값 만들기(1)
def solution(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]

#팩토리얼
def solution(n):
    output = 1
    i = 0
    while output <= n:
        i += 1
        output = output * i
        
    return i - 1
        