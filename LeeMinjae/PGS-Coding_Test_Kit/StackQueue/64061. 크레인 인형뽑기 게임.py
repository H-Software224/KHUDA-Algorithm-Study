def solution(board, moves):
    # 뽑은 인형을 쌓아두는 공간
    # 첫 경우에 대해 out of range를 방지하며 비교하기 위해 0 요소를 추가해둠
    out_board = [0]
    
    # 행, 열을 뒤집어서 리스트에 다시 저장
    board = list(map(list, zip(*board)))
    answer = 0
    
    for move in moves:
        # 뒤집은 board 리스트에 대해 index값으로 접근
        for i, b in enumerate(board[move-1]):
            # 요소가 0이 아닌 경우에만 인형을 뽑도록 조건을 추가 (요소 0 = 인형이 없다는 뜻)
            if b != 0:
                out_board.append(board[move-1][i])      # 인형을 꺼내서 out_board stack에 추가
                board[move-1][i] = 0                    # 꺼낸 곳은 인형이 없으니 0으로 변경
                
                # out_board 스택 비교
                # 가장 마지막 요소와 마지막에서 두 번째 요소가 같은 경우에만 두 요소를 꺼내고, answer값을 2 더해줌
                if out_board[-1] == out_board[-2]:
                    answer += 2
                    out_board.pop()
                    out_board.pop()
                    
                # 인형을 한번 꺼냈으면 다른 반복으로 넘어가도록 함
                break
                
    # 지금까지 꺼낸 모든 인형의 개수를 반환
    return answer
