from itertools import permutations

def solution(k, dungeons):
    answer = []
    # 순열을 사용해서 배치할 수 있는 dungeons의 모든 경우를 뽑음
    for p in list(permutations(dungeons, len(dungeons))):
        check_k = k
        count = 0
        # 각 경우마다 반복
        for d in p:
            # 유저의 현재 피로도가 최소 필요 피로도보다 크거나 같은지 체크
            if check_k >= d[0]:     # 피로도가 최소 필요도보다 크거나 같은 경우
                count += 1
                check_k -= d[1]
            else:                   # 피로도가 최소 필요도보다 작은 경우 -> 바로 break
                break
        answer.append(count)
    return max(answer)

"""
순열 안쓰고 도전 (일단 실패)
def solution(k, dungeons):
    answer = 0
    dungeons = sorted(dungeons, key=lambda x: x[1])
    dungeons = sorted(dungeons, key=lambda x: (x[0]-x[1]), reverse=True)
    print(dungeons)
    
    for d in dungeons:
        if k >= d[0]:
            answer += 1
            k -= d[1]
    return answer
"""
