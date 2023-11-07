#점의 위치 구하기
def solution(dot):
    if dot[0] > 0:
        if dot[1] > 0:
            return 1
        return 4
    if dot[1] > 0:
        return 2
    return 3

#2차원으로 만들기
def solution(num_list, n):
    answer = []
    for i in range(0,len(num_list),n):
        answer.append(num_list[i:i+n])
    return answer

#공 던지기
def solution(numbers, k):
    new_list = []
    while len(new_list) < 2*k:
        for num in numbers:
            new_list.append(num)
    return new_list[2*(k-1)]

#배열 회전시키기
def solution(numbers, direction):
    answer = numbers.copy()
    if direction == "right":
        answer[0] = numbers[-1]
        for i in range (1,len(numbers)):
            answer[i] = numbers[i-1]
    else:
        answer[-1] = numbers[0]
        for i in range (len(numbers)-1):
            answer[i] = numbers[i+1]   

    return answer