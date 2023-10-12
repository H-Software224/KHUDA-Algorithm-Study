def solution(answers):
    # 초기값 세팅
    answer = [0, 0, 0]
    supo_one = [1, 2, 3, 4, 5] * len(answers)
    supo_two = [2, 1, 2, 3, 2, 4, 2, 5] * len(answers)
    supo_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * len(answers)
    
    # answers를 반복하면서 수포자 1, 2, 3이 정답이 맞는지 체크하기
    # 인덱스를 반복시키지 않고, enumerate로 반복시키는 방법을 사용해도 된다!
    for i in range(len(answers)):
        if answers[i] == supo_one[i]: answer[0] += 1
        if answers[i] == supo_two[i]: answer[1] += 1
        if answers[i] == supo_three[i]: answer[2] += 1
        
    # 정답 맞춘 개수가 들어있는 리스트를 반복하면서, 최댓값과 일치하는지 찾기
    return [i+1 for i in range(len(answer)) if max(answer)==answer[i]]
