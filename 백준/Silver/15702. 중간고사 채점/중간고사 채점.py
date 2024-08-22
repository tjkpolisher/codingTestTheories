import sys
input = sys.stdin.readline

N, M = map(int, input().split())
scores = list(map(int, input().split()))
score_table = {i + 1: scores[i] for i in range(N)}

result_table = []
for _ in range(M):
    student_score = list(input().split())
    student_num = int(student_score[0])
    net_score = 0
    for i in range(1, N + 1):
        result = student_score[i]
        if result == 'O':
            net_score += score_table[i]
    result_table.append([student_num, net_score])

result_table.sort(key=lambda x: (-x[1], x[0]))
print(result_table[0][0], result_table[0][1])