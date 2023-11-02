def solution(numbers):
    # 1. 모든 numbers의 원소를 string으로 변경한다.
    numbers = [str(n) for n in numbers]
    
    # 2. numbers의 원소는 모두 0~1,000 사이의 값이니 최대값인 네자릿수로 만들어준다.
    # why? out of range를 방직하기 위해 (한자릿수와 네자릿수를 동일하게 비교하기 위함)
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)

    # 3. numbers 리스트를 문자열로 바꾼다.
    answer = ''.join(numbers)

    # 4. (테스트 11 예외 처리) 첫째자리가 0일 경우에는 그냥 0으로 치환
    return '0' if answer[0] == '0' else answer
