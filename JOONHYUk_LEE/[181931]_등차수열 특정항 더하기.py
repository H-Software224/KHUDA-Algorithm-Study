def solution(a, d, included):
    answer = 0
    list_deungcha = []
    for i in range(len(included)):
        list_deungcha.append(a + i * d)
    
    for j in range(len(included)):
        if included[j] == True:
            answer += list_deungcha[j] 
    return answer