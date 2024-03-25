def get_answer(n, y, width, diagonal1, diagonal2):
    ans = 0
    if y == n:
        ans += 1
    else:
        for i in range(n):
            if width[i] or diagonal1[i + y] or diagonal2[i - y + n]:
                continue
            
            width[i] = diagonal1[i + y] = diagonal2[i - y + n] = True
            
            ans += get_answer(n, y + 1, width, diagonal1, diagonal2)
            
            width[i] = diagonal1[i + y] = diagonal2[i - y + n] = False
    return ans

def solution(n):
    answer = get_answer(n, 0, [False] * n,
                       [False] * 2 * n,
                       [False] * 2 * n)
    return answer