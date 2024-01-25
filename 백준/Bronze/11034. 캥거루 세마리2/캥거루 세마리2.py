while True:
    try:
        A, B, C = map(int, input().split())
    except EOFError:
        break
    cnt = 0
    while True:
        d1, d2 = B - A, C - B
        if d1 == 1 and d2 == 1:
            print(cnt)
            break
        
        if d1 >= d2:
            C = B - 1
            B, C = C, B
        else:
            A = B + 1
            A, B = B, A
        cnt += 1