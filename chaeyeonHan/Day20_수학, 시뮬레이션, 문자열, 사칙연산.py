#직사각형 넓이 구하기
def solution(dots):
    x_list = [dots[x][0] for x in range (4) ]
    y_list = [dots[y][1] for y in range (4) ]
    return (max(x_list) - min(x_list)) * (max(y_list) - min(y_list))

#캐릭터의 좌표
def solution(keyinput, board):
    answer = [0,0]
    max_x = board[0]//2
    max_y = board[1] // 2
    for key in keyinput:
        if key == 'right' and answer[0] < max_x:
            answer[0] += 1
        elif key == 'left' and answer[0] > -max_x:
            answer[0] -= 1
        elif key == 'up' and answer[1] < max_y:
            answer[1] += 1
        elif key == 'down' and answer[1] > -max_y:
            answer[1] -= 1
    
    return answer

#최댓값 만들기 (2)
def solution(numbers):
    answer = numbers[0] * numbers[1]
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer = max(answer, numbers[i]*numbers[j])
    return answer 

#다항식 더하기
def solution(polynomial):
    sum = 0
    sum_x = 0
    terms = polynomial.split('+')
    for term in terms:
        term = term.strip()
        if term.isdigit():
            sum += int(term)
        else:
            if term[0] == 'x':
                sum_x += 1
            else:
                sum_x += int(term.rstrip('x'))
    if sum_x == 1: sum_x =''
    if sum_x == 0:
        if sum == 0:
            answer = "0"
        else:
            answer = f"{sum}"
    elif sum == 0:
        answer = f"{sum_x}x"
    else:
        answer = f"{sum_x}x + {sum}"
    return answer



