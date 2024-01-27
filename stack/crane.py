def solution(board, moves):
    # 문제 출처: 2019 카카오 개발자 겨울 인턴십
    # 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/64061
    answer = 0
    basket_stack = [] # 바구니를 나타내는 스택
    board_stacks = [[] for _ in range(len(board[0]))] # 보드의 각 열을스택화
    r, c = len(board), len(board[0])
    
    # board의 각 열을 스택화
    for i in range(c):
        for j in range(1, r + 1):
            if board[-j][i] != 0:
                board_stacks[i].append(board[-j][i])
    
    # 크레인 조작
    for m in moves:
        if board_stacks[m - 1]: # 해당 스택이 비어있지 않은 경우
            popped = board_stacks[m - 1].pop() # 맨 위의 인형 뽑기
            if basket_stack and basket_stack[-1] == popped: # 바구니가 비어있지 않고, 미리 뽑은 인형이 바구니 맨 위의 인형과 동일할 때
                basket_stack.pop()
                answer += 2 # 같은 인형이 함께 사라지므로 항상 정답이 2씩 올라갑니다.
            else: # 해당 없으면 뽑은 인형은 바구니 스택에 푸시
                basket_stack.append(popped)
    
    return answer
    

if __name__ == "__main__":
    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]
    print(solution(board, moves))