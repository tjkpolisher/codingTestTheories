import sys
input = sys.stdin.readline

N = int(input())
ratings = []
for _ in range(N):
    rating_now = sorted(list(map(int, input().split())))
    ratings.append(rating_now[N // 2])

ratings.sort()
print(ratings[N // 2])