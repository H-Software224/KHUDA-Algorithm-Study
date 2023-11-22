#7의 개수
def solution(array):
    count = 0
    for num in array:
        count += str(num).count('7')
    return count

#잘라서 배열로 저장하기
def solution(my_str, n):
    answer = []
    if len(my_str) % n == 0:
        for i in range(len(my_str)//n):
            answer.append(my_str[n * i : n * (i + 1)])
        return answer
    else:
        for i in range(len(my_str)//n + 1):
            answer.append(my_str[n * i : n * (i + 1)])
        return answer
    
#중복된 숫자 개수
def solution(array, n):
    return array.count(n)

#머쓱이보다 키 큰 사람
def solution(array, height):
    answer = 0
    for elem in array:
        if elem > height:
            answer += 1
    return answer