def solution(n):
    list1 = [n]
    # 첫번째 요소(n): list1[0] = n, 짝
    # (n = n / 2)
    # 두번째 요소(n / 2): list1[1] = n / 2, 홀
    # (n = n * 3 + 1)
    # 세번째 요소(3 * (n / 2) + 1):  list1[2] = 3 * (n / 2) + 1, 짝
    # (n = n / 2)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            list1.append(n)
        else:
            n = n * 3 + 1
            list1.append(n)
    return list1

print(solution(10))