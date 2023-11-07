def solution(board, moves):
    cnt = 0
    result_list = []

    for i in range (len(moves)):
        for j in range (len(board)):
            target_num = board[j][moves[i] - 1]
            if target_num != 0:
                if len(result_list) == 0:
                    result_list.append(target_num)
                elif result_list[-1] == target_num:
                    del result_list[-1]
                    cnt += 2
                else:
                    result_list.append(target_num)
                board[j][moves[i] - 1] = 0
                break
                
    return cnt