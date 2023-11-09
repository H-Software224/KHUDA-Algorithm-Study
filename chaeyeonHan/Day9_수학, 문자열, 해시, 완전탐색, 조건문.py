#점의 위치 구하기
def solution(hp):
    x5, y5 = divmod(hp,5)
    x3,y3 = divmod(y5,3)
    x1, y1 = divmod(y3,1)
    return x5 + x3 + x1

#모스부호(1)
def solution(letter):
    answer=''
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    letter_list = letter.split()
    for sign in letter_list:
        answer += morse[sign]
    return answer

#가위 바위 보
def solution(rsp):
    answer = ''
    for char in rsp:
        if char == '2':
            answer += '0'
        elif char == '0':
            answer += '5'
        else:
            answer += '2'
    return answer

#구슬을 나누는 경우의 수

import math
def solution(balls, share):
    return math.factorial(balls)/(math.factorial(balls - share) * math.factorial(share))