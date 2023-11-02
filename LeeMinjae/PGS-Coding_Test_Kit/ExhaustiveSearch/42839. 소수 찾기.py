from itertools import permutations

def solution(numbers):
    answer = 0
    
    candits = set()
    numbers = list(map(str, numbers))

    # numbers 숫자 조합하기
    for i in range(1, len(numbers)+1):
        # 1. 순열을 이용해서 1부터 len(numbers)까지 숫자를 증가시키면서 순서대로 뽑는다.
        permute = permutations(numbers, i)
        # 2. map을 이용해서 permute 리스트 요소들을 묶어준다.
        permute = set(map(lambda x: int(''.join(x)), permute))
        # 3. 기존 집합에서 교집합으로 남겨둔다.
        candits = candits.union(permute)
    # 4. 0 제거 시키기
    candits = [num for num in list(candits) if num > 1]

    for num in candits:
        isSosu = True
        if num == 1:
            isSosu = False
            break
        for i in range(2, num//2+1):
            if num % i == 0:
                isSosu = False
                break
        if isSosu: answer += 1
    
    return answer
