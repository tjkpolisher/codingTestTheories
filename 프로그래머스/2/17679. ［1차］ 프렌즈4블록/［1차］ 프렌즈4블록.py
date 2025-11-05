def solution(m, n, board):
    answer = 0
    
    # 1. board를 2차원 리스트로 변환
    for i in range(len(board)):
        board[i] = list(board[i])
    
    # 2. 블록 찾고 제거하기
    def find_and_remove():
        remove = [[False] * n for _ in range(m)]
        
        # 2-1. 모든 위치에서 2x2 블록 확인
        for i in range(m - 1):
            for j in range(n - 1):
                if (board[i][j] != '0' and
                    board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]):
                    remove[i][j] = True
                    remove[i][j + 1] = True
                    remove[i + 1][j] = True
                    remove[i + 1][j + 1] = True
        
        # 2-2. 제거할 블록 제거 및 개수 세기
        cnt = 0
        for i in range(m):
            for j in range(n):
                if remove[i][j]:
                    board[i][j] = '0'
                    cnt += 1
        
        # 2-3. 블록 아래로 떨어뜨리기
        for j in range(n):
            write_idx = m - 1
            for i in range(m - 1, -1, -1):
                if board[i][j] != '0':
                    if i != write_idx:
                        board[write_idx][j] = board[i][j]
                        board[i][j] = '0'
                    write_idx -= 1
        
        return cnt
    
    # 3. 더 깨트릴 블록이 없을 때까지 bfs 반복
    while True:
        tmp = find_and_remove()
        if not tmp:
            break
        answer += tmp
    
    return answer