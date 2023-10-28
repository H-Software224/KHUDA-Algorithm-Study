def solution(numLog):
    result = ''
    
    for i in range(len(numLog) - 1):
        log = numLog[i + 1] - numLog[i]
        if log == 1:
            result += 'w'
        elif log == -1:
            result += 's'
        elif log == 10:
            result += 'd'
        elif log == -10:
            result += 'a'
    return result