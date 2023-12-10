N = int(input())
scores = list(map(int, input().split()))

M = max(scores)
max_index = scores.index(M)
for i in range(N):
    scores[i] = scores[i] / M * 100
print(sum(scores) / N)