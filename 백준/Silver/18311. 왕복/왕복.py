import sys
input = sys.stdin.readline

N, K = map(int, input().split())
courses = list(map(int, input().split()))
courses = courses + courses[::-1]

distance = [0]
d = 0
for c in courses:
    d += c
    distance.append(d)

course_num = list(range(1, N + 1))
course_num = course_num + course_num[::-1]

ans = 1
for i in range(1, 2 * N):
    if distance[i - 1] <= K < distance[i]:
        ans = course_num[i - 1]
        break
print(ans)