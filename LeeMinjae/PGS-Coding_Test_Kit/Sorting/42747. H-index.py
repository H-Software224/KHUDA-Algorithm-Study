def solution(citations):
    answer = 0
    for i in sorted(citations, reverse=True):
        if i>answer: answer += 1
    return answer
