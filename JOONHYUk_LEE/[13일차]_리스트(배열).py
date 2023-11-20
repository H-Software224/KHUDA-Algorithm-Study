# 181892 n번째 원소부터
def solution(num_list, n):
    return num_list[n - 1:]

# 181891 순서 바꾸기
def solution(num_list, n):
    new_list1 = num_list[n:] + num_list[:n]
    return new_list1

# 181890 왼쪽 오른쪽
def solution(str_list):
    for i in range(len(str_list)):
        if str_list[i] == 'l':
            return str_list[:i]
        elif str_list[i] == 'r':
            return str_list[i + 1:]
    return []

# 181889 n번째 원소까지
def solution(num_list, n):
    return num_list[:n]

# 181888 n개 간격의 원소들
def solution(num_list, n):
    return num_list[::n]

