N, K = map(int, input().split())

cnt = 0
for i in range(N + 1):
    for j in range(60):
        for k in range(60):
            ts = [str(i).zfill(2), str(j).zfill(2), str(k).zfill(2)]
            string = ''.join(ts)
            if str(K) in string:
                cnt += 1
print(cnt)