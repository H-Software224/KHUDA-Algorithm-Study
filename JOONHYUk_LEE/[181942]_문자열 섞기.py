def solution(str1, str2):
    result = ''
    
    for i in range(len(str1)):
        result += f'{str1[i]}{str2[i]}'
    return result 
            
        