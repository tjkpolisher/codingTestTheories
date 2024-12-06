import sys
input = sys.stdin.readline

n, k = map(int, input().split())
grades = []
for _ in range(n):
    grades.append(int(input()))

grades.sort(reverse=True)

print(sum(grades[:k]))