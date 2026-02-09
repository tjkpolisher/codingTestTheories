def solution(data, col, row_begin, row_end):
    """
    data: 2차원 행렬(행은 튜플, 열은 컬럼)
    첫 번째 컬럼은 기본키(즉, 중복 없음).
    """
    answer = 0
    
    # 1. col번째 컬럼으로 오름차순 정렬(동일하면 기본키 기준 내림차순 정렬)
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    
    # 2. row_begin부터 row_end까지 s_i 계산 및 누적
    for i in range(row_begin - 1, row_end):
        s_i = 0
        for d in data[i]:
            s_i += d % (i + 1)
        # 3. bitwise XOR 연산
        answer ^= s_i
    return answer