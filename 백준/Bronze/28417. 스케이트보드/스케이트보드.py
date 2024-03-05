N = int(input())
max_score = 0

for _ in range(N):
    scores = list(map(int, input().split()))
    run = max(scores[:2])
    trick = sorted(scores[2:], reverse=True)[:2]
    total_score = run + sum(trick)
    if total_score > max_score:
        max_score = total_score

    if total_score == 300:
        break

print(max_score)