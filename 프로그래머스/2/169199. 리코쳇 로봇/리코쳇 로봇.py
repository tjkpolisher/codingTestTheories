from collections import deque
def solution(board):
    # 1. 시작 위치와 목표 위치 탐색
    len1 = len(board)
    len2 = len(board[0])
    R = None
    dist = [[10 ** 9 for _ in range(len2)] for _ in range(len1)]
    
    for i in range(len1):
        for j in range(len2):
            if board[i][j] == 'R':
                R = (i, j, 0)
            if R:
                break
        if R:
            break
    
    # 2. BFS 실행
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append(R)
    
    while q:
        x, y, cnt = q.popleft()
        # 3-1. G에 도착한 경우 이동 횟수 반환
        if board[x][y] == 'G':
            return cnt
        
        # 3-2. 네 방향 탐색
        for i in range(4):
            nx = x
            ny = y
            while 0 <= nx + dx[i] < len1 and 0 <= ny + dy[i] < len2 and board[nx + dx[i]][ny + dy[i]] != 'D':
                nx += dx[i]
                ny += dy[i]
            # 3-3. 도달한 적 없거나, 이전에 도달한 경우보다 적은 이동 횟수로 도달 시 갱신
            if dist[nx][ny] > cnt + 1:
                dist[nx][ny] = cnt + 1
                q.append((nx, ny, cnt + 1))
    
    # 도달 불가 시 -1을return
    return -1