def solution(rows, columns, queries):
    answer = []
    
    # 0. 초기 행렬 생성
    matrix = [
        [i * columns + j + 1 for j in range(columns)]
        for i in range(rows)
    ]
    
    # 1. 쿼리마다 연산
    for query in queries:
        # 2. 범위 책정
        # 문제의 좌표는 1-indexed이므로 0-indexed로 변환
        start = [query[0] - 1, query[1] - 1]
        end = [query[2] - 1, query[3] - 1]
        
        x1, y1 = start
        x2, y2 = end
        
        coords = []
        tmp = []
        
        # 3. 회전 범위에 해당하는 테두리 좌표들을 시계 방향 순서로 모으기
        # 위쪽 변: 왼쪽 -> 오른쪽
        for y in range(y1, y2 + 1):
            coords.append((x1, y))
        
        # 오른쪽 변: 위 -> 아래
        for x in range(x1 + 1, x2 + 1):
            coords.append((x, y2))
        
        # 아래쪽 변: 오른쪽 -> 왼쪽
        for y in range(y2 - 1, y1 - 1, -1):
            coords.append((x2, y))
        
        # 왼쪽 변: 아래 -> 위
        for x in range(x2 - 1, x1, -1):
            coords.append((x, y1))
        
        # 4. 테두리에 있는 숫자들을 모으기
        for x, y in coords:
            tmp.append(matrix[x][y])
        
        # 5. 이동한 숫자들 중 최솟값 저장
        answer.append(min(tmp))
        
        # 6. 시계 방향으로 한 칸 회전
        # coords 순서가 시계 방향이므로,각 위치는 바로 이전 위치의 값을 받으면 됨
        rotated = [tmp[-1]] + tmp[:-1]
        
        for (x, y), value in zip(coords, rotated):
            matrix[x][y] = value
    
    return answer