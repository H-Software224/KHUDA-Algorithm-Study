# 181897 리스트 자르기
def solution(n, slicer, num_list):
    answer = []
    a, b, c = slicer
    if n == 4: 
        return num_list[a:b + 1:c]
    elif n == 3:
        return num_list[a:b + 1]
    elif n == 2:
        return num_list[a:]
    elif n == 1:
        return num_list[:b+1]

# 181896 첫 번째로 나오는 음수
def solution(num_list):
    result =0 
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1

# 181895 배열 만들기
def solution(arr, intervals):
    answer = []
    for sub_int in intervals:
        # interval 내에 있는 각각의 구간에 대해 arr 배열을 잘라야 함.
        a, b = sub_int
        answer += arr[a:b+1]
    return answer

# 181894
def solution(arr):
    answer = []
    fir = 0
    last = 0
    # 처음 2가 나오면 새로운 배열에 arr의 요소를 하나씩 반복하면서 입력.
    # 2가 하나 뿐이면 [2] 를 return 
    # 2가 없으면 [-1]을 return
    # 다음 2인 i 인덱스를 answer에 더함. 
    # 중요한 건 첫 번째 2 바로 다음 2까지의 배열이 아닌, 배열의 마지막 2가 return의 끝이라는 점. 
    for i in range(len(arr)):
        if arr[i] == 2:
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    elif len(answer) == 1:
        return [2]
    else:
        fir = answer[0]
        last = answer[-1] + 1
        return arr[fir:last]

# 181893 배열 조각하기 - 문제 코드
def solution(arr, query):
    result = []
    # query 정수 순회
    # arr 배열의 query[i] 번째 index를 찾고 기존의 배열에서 뒷부분, 앞부분 삭제
    for i in range(len(query)):
        if i % 2 == 0:
            index = query[i] + 1
            arr = arr[:index]
        else:
            index = query[i]
            arr = arr[index:]
    return arr