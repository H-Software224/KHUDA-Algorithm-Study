def solution(arr, queries):
    
    for a, b in queries:
        arr[a], arr[b] = arr[b], arr[a]
    return arr
    '''for k in queries:
        for l in range(len(k) - 1):
            temp = arr[k[l]]
            arr[k[l]] = arr[k[l + 1]]
            arr[k[l+1]] = temp
    return arr'''