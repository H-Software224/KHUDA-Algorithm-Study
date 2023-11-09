#1. 피자 나눠 먹기(1)
def solution(n):
    return n//7 if n%7==0 else n//7+1

#2. 피자 나눠 먹기(2)
import math
def solution(n):
    lcm = n * 6 //math.gcd(n,6)
    return lcm / 6

#3. 피자 나눠 먹기(3)
def solution(slice, n):
    while n % slice !=0 :
        n+=1
    return n // slice

#4. 배열의 평균값
def solution(numbers):
    return sum(numbers)/len(numbers)