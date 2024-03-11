esm = list(map(int, input().split()))
calendar = [1, 1, 1]
ans = 1
while True:
    if calendar == esm:
        print(ans)
        break

    ans += 1
    for i in range(3):
        calendar[i] += 1

    if calendar[0] > 15:
        calendar[0] = 1
    if calendar[1] > 28:
        calendar[1] = 1
    if calendar[2] > 19:
        calendar[2] = 1