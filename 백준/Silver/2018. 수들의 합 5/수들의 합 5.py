N = int(input())

if N == 1 or N == 2:
    print(1)
else:
    start = 1
    end = 1
    total = 1
    cnt = 1

    while end < N // 2 + 2:
        if total == N:
            cnt += 1
            end += 1
            total += end
        elif total < N:
            end += 1
            total += end
        else:
            total -= start
            start += 1

    print(cnt)