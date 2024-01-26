N, K = map(int, input().split())
numbers = set(range(2, N + 1))
cnt = 0
while True:
    p = list(numbers)[0]
    to_be_removed = list(range(p, N + 1, p))
    for n in to_be_removed:
        if n in numbers:
            numbers -= set([n])
            cnt += 1
        if cnt == K:
            answer = n
            break
    if cnt == K:
        break
print(answer)