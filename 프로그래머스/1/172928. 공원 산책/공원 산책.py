def solution(park, routes):
    # 1. 시작 위치 탐색
    H = len(park)
    W = len(park[0])
    
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                y = i
                x = j
                break
            
    
    dir_table = {'S': (1, 0), 'N': (-1, 0),
                 'W': (0, -1), 'E': (0, 1)}
    # 2. 이동 방향에 따라 강아지 이동
    for route in routes:
        op, n = route.split()
        n = int(n)
        
        dy, dx = dir_table[op]
        
        # 이동 경로의 모든 칸이 유효한지 검증
        valid = True
        for step in range(1, n + 1):
            ny = y + dy * step
            nx = x + dx * step
            
            # 공원 밖으로 나가는지 확인
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                valid = False
                break
            
            # 장애물을 만나는지 확인
            if park[ny][nx] == 'X':
                valid = False
                break
        
        # 이동이 가능한 경우에만 위치 업데이트
        if valid:
            y += dy * n
            x += dx * n
    
    return [y, x]