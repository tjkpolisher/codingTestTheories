import sys
input = sys.stdin.readline

n = int(input())
ratings = []
for _ in range(n):
    ratings.append(int(input()))

ratings.sort()

min_team_ratings = []
for i in range(n // 2):
    min_team_ratings.append(ratings[i] + ratings[n - 1 - i])

print(min(min_team_ratings))