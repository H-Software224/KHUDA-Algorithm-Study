def solution(my_string, index_list):
    answer = []
    list1 = list(my_string)
    
    for i in range(len(index_list)):
        answer.append(list1[index_list[i]])
            
    return ''.join(answer)