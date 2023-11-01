def solution(n, wires):
    ans = n
    
    # wires 반복하면서 하나씩 연결 제거
    for delete_wires in (wires[i+1:] + wires[:i] for i in range(len(wires))):
        # 기준값은 연결 하나를 제거한 배열의 첫번째 요소
        s = set(delete_wires[0])
        
        # 기준값과 교집합(&)이 있는 경우에 대해 요소를 추가
        # 집합(set)을 사용해서 중복값 방지
        [s.update(w) for w in delete_wires if set(w) & s]

        # 절대값을 기준으로 가장 작은 값을 고른다 = 두 전력망이 가지고 있는 송전탑 개수의 차이 (절대값)
        ans = min(ans, abs(2 * len(s) - n))
    return ans
