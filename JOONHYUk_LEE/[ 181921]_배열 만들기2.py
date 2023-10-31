def solution(l, r):
    answer = []
    
    # 오로지 0과 5로만 이루어진 숫자여야 함. 
    # ex) 5 이상 555 이하 숫자. 5, 50, 55, 500, 505, 550, 555
    temp = [i for i in range(l, r+ 1) if (i % 5 == 0)]
    except_num = ['0', '5']
    for num in temp:
        if not set(str(num)) - set(except_num):
            answer.append(num)
    if not answer:
        return [-1]
    return answer

print(solution(5, 555))