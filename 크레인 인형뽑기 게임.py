def solution(board, moves):
    answer = 0

    stack = []

    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] != 0:
                if stack != [] and stack[-1] == board[i][move - 1]:
                    board[i][move - 1] = 0
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[i][move - 1])
                    board[i][move - 1] = 0
                break

    return answer

#회고
#for i in range(len(board)): 이 부분 범위를 멋대로 5로 잡아버렸다...
#stack[-1] 활용