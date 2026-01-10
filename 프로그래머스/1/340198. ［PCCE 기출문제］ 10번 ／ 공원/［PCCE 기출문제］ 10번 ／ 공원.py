def solution(mats, park):
    mats.sort(reverse=True)
    
    rows = len(park)
    cols = len(park[0])
    
    dp = [[0] * cols for _ in range(rows)]
    max_square = 0
    
    for i in range(rows):
        for j in range(cols):
            if park[i][j] == "-1":
                if i == 0 or j == 0:
                    # 첫 행이나 첫 열이면 1
                    dp[i][j] = 1
                else:
                    # 점화식: 왼쪽, 위, 왼쪽 대각선 중 최솟값 + 1
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
                max_square = max(max_square, dp[i][j])
    
    # mats를 내림차순 정렬해서 가능한 가장 큰 돗자리 찾기
    mats.sort(reverse=True)
    
    for mat in mats:
        if mat <= max_square:
            return mat
    
    return -1