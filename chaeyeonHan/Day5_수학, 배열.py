#옷가게 할인 받기
def solution(price):
        if 100000 <= price < 300000:
            return int(price * 0.95)
        elif 300000 <= price < 500000:
            return int(price * 0.9)
        elif price >= 500000:
            return int(price * 0.8)
        else:
            return price
        
#아이스아메리카노
def solution(money):
    num = money//5500
    change = money % 5500
    answer = [num, change]
    return answer

#나이 출력
def solution(age):
    return 2022 - age + 1

#배열 뒤집기
def solution(num_list):
    rev_list = []
    for i in range(len(num_list)):
        rev_list.append(num_list[len(num_list)-1-i])
    return rev_list