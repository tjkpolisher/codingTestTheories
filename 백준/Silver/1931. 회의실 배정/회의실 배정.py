import sys
input = sys.stdin.readline

N = int(input().rstrip())
time_table = []
for i in range(N):
    t1, t2 = map(int, input().rstrip().split())
    time_table.append([t1, t2])

time_table.sort(key=lambda x: (x[1], x[0]))

ans = 0
end_time = 0
for i, j in time_table:
    if end_time <= i:
        ans += 1
        end_time = j
print(ans)