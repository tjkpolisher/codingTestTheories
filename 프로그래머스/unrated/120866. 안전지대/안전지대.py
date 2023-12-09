def solution(board):
    N = len(board)
    dx = [-1, 1, 0, 0, -1, -1, 1, 1] # 여덟 방향 탐색
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    
    # 지뢰 설치
    mine = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                mine.append((i,j)) # 지뢰일 때의 인덱스 삽입
                
    # 지뢰가 설치된 곳 주변에 폭탄 설치
    for x, y in mine:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny] = 1

    # 폭탄이 설치되지 않은 곳만 카운팅
    count = 0
    for x in range(N):
        for y in range(N):
            if board[x][y] == 0:
                count += 1
    return count