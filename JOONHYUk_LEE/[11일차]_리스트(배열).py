# 181902 문자 개수 세기
def solution(my_string):
    result = []
    result = [0 for i in range(52)]
    # A = 65, a = 97 (아스키 코드) , ord(str) -> 문자의 아스키 코드(정수값)를 리턴.
    for i in my_string:
        if i.isupper(): num = 65
        else: num = 71
        result[ord(i) - num] += 1
    return result

# 181901 배열 만들기1
def solution(n, k):
    answer = []
    for i in range(1, n + 1):
        if i % k == 0:
            answer.append(i)
    return answer

# 181900 글자 지우기
def solution(my_string, indices):
    answer = ''
    list1 = list(my_string)
    
    for j in indices:
        list1[j] = ""
    answer = ''.join(list1)
    return answer

# 181899 카운트 다운
def solution(start, end_num):
    answer = []
    return [i for i in range(start, end_num -1, -1)]

# 181898 가까운 1 찾기
def solution(arr, idx):
    answer = 0
    idx_list = []
    for i in range(len(arr)):
        if (i >= idx) & (arr[i] == 1):
            idx_list.append(i)
    if len(idx_list) > 0:
        return min(idx_list)
    return -1