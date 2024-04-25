import sys
input = sys.stdin.readline

N = int(input())
work_table = dict()
work_time = [4, 6, 4, 10]
for _ in range(N):
    for i in range(4):
        in_service = list(input().rstrip().split())
        for s in in_service:
            if s != '-':
                if s not in work_table:
                    work_table[s] = work_time[i]
                else:
                    work_table[s] += work_time[i]

# 근무 시간이 없는 경우도 공평하다고 취급
if not work_table:
    print("Yes")
else:
    times = list(work_table.values())
    if max(times) - min(times) > 12:
        print("No")
    else:
        print("Yes")