import sys
input = sys.stdin.readline

N, M = map(int, input().split())
streaming_table = {}
real_Vtuber = []
weeks = M // 7

for _ in range(N):
    name, day, start, end = input().rstrip().split()
    day = int(day)
    week_idx = (day - 1) // 7
    sh, sm = map(int, start.split(':'))
    eh, em = map(int, end.split(':'))

    streaming_time = (eh * 60 + em) - (sh * 60 + sm)
    streaming_time *= 60

    if name not in streaming_table:
        streaming_table[name] = {
            "time": [0] * weeks,
            "day": [0] * weeks
        }

    streaming_table[name]["time"][week_idx] += streaming_time
    streaming_table[name]["day"][week_idx] += 1

for name, value in streaming_table.items():
    stream_time, stream_day = value["time"], value["day"]

    is_real = True
    for i in range(weeks):
        if stream_time[i] < 60 * 3600 or stream_day[i] < 5:
            is_real = False
            break

    if is_real:
        real_Vtuber.append(name)

if not real_Vtuber:
    print(-1)
else:
    real_Vtuber.sort()
    for Vtuber in real_Vtuber:
        print(Vtuber)