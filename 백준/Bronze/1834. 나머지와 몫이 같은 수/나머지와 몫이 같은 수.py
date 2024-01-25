N = int(input())
answer = 0
for i in range(1, N):
    answer += (i * N + i)
print(answer)