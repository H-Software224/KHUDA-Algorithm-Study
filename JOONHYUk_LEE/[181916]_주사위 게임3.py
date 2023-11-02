def solution(a, b, c, d):
    
    list1 = [a, b, c, d]
    counts = [list1.count(i) for i in list1]
    
    if max(counts) == 4:
        return a * 1111
    elif max(counts) == 3:
        p = list1[counts.index(3)]
        q = list1[counts.index(1)]
        return (10 * p + q) ** 2
    elif max(counts) == 2:
        if min(counts) == 2:
            return ((a + b) * abs(a - b)) if a == c else ((a + c) * abs(a - c)) 
        else:
            p = list1[counts.index(2)]
            return (a * b * c * d) / p ** 2
    else:
        return min(list1)
    
# 질문하기, 답지 참고.