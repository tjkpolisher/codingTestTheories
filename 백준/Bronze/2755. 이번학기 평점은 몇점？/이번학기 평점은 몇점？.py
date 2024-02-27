n = int(input())

answer = 0
scores = 0
gpa_table = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
             'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
             'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
             'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
             'F': 0.0}

for _ in range(n):
    subject, score, gpa = input().split()
    score = int(score)
    scores += score
    gpa_score = gpa_table[gpa]
    answer += score * gpa_score

answer /= scores

print(f"{round(answer + 0.0001, 2):.2f}")