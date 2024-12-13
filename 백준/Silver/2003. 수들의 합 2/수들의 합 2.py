N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for i in range(N):
    suffix_sum = 0
    for j in range(i, N):
        suffix_sum += A[j]
        if suffix_sum == M:
            cnt += 1
            break
        elif suffix_sum > M:
            break
    else:
        if suffix_sum < M:
            break
print(cnt)