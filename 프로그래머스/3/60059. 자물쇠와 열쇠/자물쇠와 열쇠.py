def rotate(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, 2 * lock_length):
        for j in range(lock_length, 2 * lock_length):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)  # 행의 길이
    m = len(key)  # 열의 길이
    
    # 자물쇠 주변에 패딩을 추가해 기존의 3배 크기로 늘림
    new_lock = [[0] * (3 * n) for _ in range(3 * n)]
    
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
    
    for rotation in range(4):
        key = rotate(key)  # 열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                # 열쇠 끼워넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 새 자물쇠에 열쇠가 들어맞으면 True 리턴 후 종료
                if check(new_lock):
                    return True
                # 안 맞으면 열쇠 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False