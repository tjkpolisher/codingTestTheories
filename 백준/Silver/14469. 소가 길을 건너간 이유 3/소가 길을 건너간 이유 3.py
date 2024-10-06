N = int(input())
t = 0
times = []
for _ in range(N):
    times.append(list(map(int, input().split())))

times.sort(key=lambda x: x[0])
for i in range(N):
    t_arrive, t_test = times[i]
    if t <= t_arrive:
        t = t_arrive + t_test
    else:
        t += t_test

print(t)