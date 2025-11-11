def solution(arr):
    answer = [0, 0]
    n = len(arr)  # 배열 arr의 크기
    
    def compress(x, y, n):
        # 1. 현재 영역의 첫 번째 값을 기준으로 모든 값이 같은지 검사
        start_val = arr[x][y]
        is_uniform = True
        
        for i in range(x, x + n):
            for j in range(y, y + n):
                # 영역 내의 값이 첫 번째 값과 다르면, 압축 실패
                if arr[i][j] != start_val:
                    is_uniform = False
                    break
            if not is_uniform:
                break
        
        # 2. 검사 결과에 따라 처리
        if is_uniform:
            # 2-1. (Base Case) 영역이 모두 같은 값일 경우
            # 해당 값의 카운트를 1 증가시키고 재귀 종료
            answer[start_val] += 1
        else:
            # 2-2. (Recursive Step) 영역이 섞여 있을 경우
            # 4개의 정사각형으로 쪼개어 각각에 대해 재귀 호출
            new_size = n // 2
            
            compress(x, y, new_size)                      # 1사분면 (좌측 상단)
            compress(x, y + new_size, new_size)          # 2사분면 (우측 상단)
            compress(x + new_size, y, new_size)          # 3사분면 (좌측 하단)
            compress(x + new_size, y + new_size, new_size) # 4사분면 (우측 하단)

    # 3. 전체 배열(0, 0)에서 시작, 배열의 크기 n
    compress(0, 0, n)
    
    return answer