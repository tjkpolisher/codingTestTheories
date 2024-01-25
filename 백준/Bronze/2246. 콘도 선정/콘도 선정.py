N = int(input())
condos = []
for i in range(N):
    D, C = map(int, input().split())
    condos.append([D, C])
condos.sort(key=lambda x:(x[0], x[1]))

cost = 10001
answer = 0
for condo in condos:
    current = condo[1]
    if current < cost:
        cost = current
        answer += 1
print(answer)