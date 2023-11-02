def solution(arr, queries):
    result = []
    for query in queries:
        for i in range(query[0], query[1] + 1):
            if i % query[2] == 0:
                arr[i] += 1
    return arr

print(solution([0, 1, 2, 4, 3], [[0, 4, 1],[0, 3, 2],[0, 3, 3]]))