# 181887 홀수 vs 짝수
def solution(num_list):
    """hol = 0
    jaq = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            jaq += num_list[i]
        else:
            hol += num_list[i]             
    return max(hol, jaq)
    """
    hol = sum(num_list[1::2])
    jaq = sum(num_list[::2])
    return max(hol, jaq)

# 181886 5명씩
def solution(names):
    return(names[::5])

# 181885 할 일 목록
def solution(todo_list, finished):
        
    """
    dic1 = {}
    result = []
    for i in range(len(todo_list)):
        dic1[todo_list[i]] = finished[i]
    print(dic1)
    for key, value in dic1.items():
        if value == False:
            result.append(key)
    return result
    """
    return [work for idx, work in enumerate(todo_list) if finished[idx] == False]

# 181884 n보다 커질 때까지 더하기
def solution(numbers, n):
    result = 0
    for i in numbers:
        result += i
        if result > n:
            break
    return result

# 181883 수열과 구간 쿼리1
def solution(arr, queries):
    """
    for query in queries:
        s, e = query[0], query[1]
        for i in range(len(arr)):
            if i >= s and i <= e:
                arr[i] += 1
    return arr
    """
    for s, e in queries:
        for i in range(s, e + 1):
            arr[i] += 1
    return arr