N, X = map(int, input().split())
visitor = list(map(int, input().split()))
sum_visitor = {}
answer = 0
partial_sum = sum(visitor[:X - 1])

for i in range(N - X + 1):
    partial_sum += visitor[i + X - 1]

    if partial_sum not in sum_visitor:
        sum_visitor[partial_sum] = 1
    else:
        sum_visitor[partial_sum] += 1

    if answer < partial_sum:
        answer = partial_sum
    partial_sum -= visitor[i]

if not answer:
    print('SAD')
else:
    print(answer)
    print(sum_visitor[answer])