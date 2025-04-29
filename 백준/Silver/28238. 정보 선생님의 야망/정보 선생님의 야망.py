import sys
input = sys.stdin.readline

n = int(input())

max_cnt = -1
best_days = [[0] * 5 for _ in range(5)]

for _ in range(n):
    student = list(map(int, input().split()))
    for i in range(5):
        if student[i] == 1:
            for j in range(i + 1, 5):
                if student[j] == 1:
                    best_days[i][j] += 1

best_1, best_2 = 0, 1
for i in range(5):
    for j in range(i + 1, 5):
        if best_days[i][j] > max_cnt:
            max_cnt = best_days[i][j]
            best_1, best_2 = i, j

days = [0] * 5
days[best_1], days[best_2] = 1, 1

print(max_cnt)
print(*days)