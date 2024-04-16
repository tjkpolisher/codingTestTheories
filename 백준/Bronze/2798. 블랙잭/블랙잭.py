import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()
result = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            tmp = cards[i] + cards[j] + cards[k]
            if tmp > M:
                pass
            else:
                result = max(result, tmp)

print(result)