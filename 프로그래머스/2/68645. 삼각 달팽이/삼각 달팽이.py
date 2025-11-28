def solution(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2, 3]
    elif n == 3:
        return [1, 2, 6, 3, 4, 5]

    answer = [[0] * i + [0] for i in range(1, n + 1)]  # 반환할 행렬
    answer.append([0] * (n + 1))
    
    i = 0
    j = 0
    num = 1
    
    flag1 = True  # 변 1 (초기 진행 방향)
    flag2 = False  # 변 2
    flag3 = False  # 변 3
    
    while True:
        answer[i][j] = num
        num += 1
        if flag1 and (i == n - 1 or answer[i + 1][j]):
            flag1 = False
            flag2 = True
        elif flag2 and (j == n - 1 or answer[i][j + 1]):
            flag2 = False
            flag3 = True
        elif flag3 and answer[i - 1][j - 1]:
            flag3 = False
            flag1 = True
        
        # 종료 조건
        if answer[i + 1][j] and answer[i][j + 1] and answer[i - 1][j - 1]:
            break
        
        if flag1:
            i += 1
        elif flag2:
            j += 1
        else:
            i -= 1
            j -= 1
    
    arr = []
    for i in range(n):
        for j in range(i + 1):
            arr.append(answer[i][j])
    
    return arr