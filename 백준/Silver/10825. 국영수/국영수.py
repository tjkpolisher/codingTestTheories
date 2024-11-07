import sys
input = sys.stdin.readline

N = int(input())
total_list = []
for _ in range(N):
    name, score1, score2, score3 = input().rstrip().split()
    score1 = int(score1)
    score2 = int(score2)
    score3 = int(score3)
    total_list.append([name, score1, score2, score3])

total_list.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for t in total_list:
    print(t[0])