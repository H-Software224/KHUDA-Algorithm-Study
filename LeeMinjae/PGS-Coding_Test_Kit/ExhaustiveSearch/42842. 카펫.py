def solution(brown, yellow):
    # 카펫을 만들 수 있는 조합 만들기
    mul_list = []
    for i in range(1, brown+yellow+1):
        if (brown+yellow)%i == 0:
            mul_list.append([i, int((brown+yellow)/i)])
    
    # 해당 조합의 카펫으로 brown, yellow를 만들 수 있는지 체크
    for ml in mul_list:
        width, height = ml[0], ml[1]
        
        # 조건 1. 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 길다는 조건 만족
        # 조건 2. 가로 세로로 카펫을 그렸을 때, yellow 개수가 같아야 함
        if (width >= height) and (width-2)*(height-2)==yellow:
            return [width, height]
