"""
사전순서는 word 길이 + hidden_number로 구할 수 있다.

1. "AAAAE"의 result는 6, word 길이 5 + hidden number 1
2. "AAAE"의 result는 10, word 길이 4 + hidden number 6
3. "AAE"의 result는 34, word 길이 3 + hidden number 31
"""

def solution(word):
    answer = len(word)
    char = ["A", "E", "I", "O", "U"]
    hidden_number = [781, 156, 31, 6, 1]
    
    for i, v in enumerate(word):
        answer += (char.index(v)) * hidden_number[i]
    return answer
