def solution(commands):
    answer = []
    
    # merged: 셀이 병합되지 않았을 때는 그 자신의 인덱스를, 병합 후에는 (r1, c1) 위치의 값을 표시하는 테이블
    merged = [[(i, j) for j in range(50)] for i in range(50)]
    # table: 실제 값이 저장되는 테이블 (아무것도 없을 때는 "EMPTY" 처리)
    table = [["EMPTY"] * 50 for _ in range(50)]
    
    for command in commands:
        # UPDATE 명령어 (1, 2번 케이스)
        if command.startswith('UPDATE'):
            command = command.split()
            if len(command) == 4:
                # 1번 케이스
                r, c, value = command[1], command[2], command[3]
                # r, c는 정수형으로 변환 필요 (이하 과정에서도 반복적으로 적용됨)
                r, c = int(r) - 1, int(c) - 1
                x, y = merged[r][c]
                table[x][y] = value
            
            elif len(command) == 3:
                # 2번 케이스
                value1, value2 = command[1], command[2]
                # value1을 갖는 셀을 완전 탐색을 통해 탐색 - 이중 반복문
                # 시간 정확도 O(N^2)이지만, 최악의 경우에도 연산이 2500회이므로 시간적 부담 없음
                for i in range(50):
                    for j in range(50):
                        if table[i][j] == value1:
                            table[i][j] = value2
        
        # 3번 케이스 (MERGE 명령어)
        elif command.startswith('MERGE'):
            _, r1, c1, r2, c2 = command.split()
            # 셀 번호가 1부터 시작하므로, 0부터 시작하는 인덱스에 맞추기 위해 1씩 뺌
            r1, c1 = int(r1) - 1, int(c1) - 1
            r2, c2 = int(r2) - 1, int(c2) - 1
            
            x1, y1 = merged[r1][c1]
            x2, y2 = merged[r2][c2]
            
            # 두 셀 중 한 셀이 값을 가지고 있을 경우 병합된 셀은 그 값을 가짐
            if table[x1][y1] == "EMPTY":
                table[x1][y1] = table[x2][y2]
            # 병합된 셀 간의 종속 관계를 인덱스로 표현
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x2, y2):
                        merged[i][j] = (x1, y1)
        
        # 4번 케이스 (UNMERGE 명령어)
        elif command.startswith('UNMERGE'):
            _, r, c = command.split()
            r, c = int(r) - 1, int(c) - 1
            x, y = merged[r][c]
            previous_value = table[x][y]  # 병합 해제 후 셀이 가져갈 값
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x, y):
                        merged[i][j] = (i, j)
                        table[i][j] = "EMPTY"  # (r, c) 외의 셀은 빈 셀이 됨
            table[r][c] = previous_value  # (r, c) 위치의 셀이 값을 가져감
        
        # 5번 케이스 (PRINT 명령어)
        elif command.startswith('PRINT'):
            _, r, c = command.split()
            r, c = int(r) - 1, int(c) - 1
            x, y = merged[r][c]
            answer.append(table[x][y])
    return answer