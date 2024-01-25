while True:
    B, N = map(int, input().split())
    if B == N == 0:
        break
    
    A = 1
    diff_previous = 1000000
    while True:
        diff = abs(A ** N - B)
        if diff > diff_previous:
            A -= 1
            break
        else:
            diff_previous = diff
            A += 1
    print(A)