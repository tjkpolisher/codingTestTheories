def solution(n, w, num):
    boxes = [[0] * w for _ in range(n // w + 1)]
    cnt = 1
    x, y = 0, 0
    if w == 1:
        return n - num + 1

    for i in range(n // w + 1):
        for j in range(w):
            boxes[i][j] = cnt
            if cnt == num:
                x, y = i, j
            if cnt == n:
                break
            cnt += 1
        if i % 2 == 1:
            boxes[i] = boxes[i][::-1]
    
    if x % 2 == 1:
        y = w - y - 1

    answer = (n // w + 1) - x
    if boxes[-1][y] == 0:
        answer -= 1
    return answer