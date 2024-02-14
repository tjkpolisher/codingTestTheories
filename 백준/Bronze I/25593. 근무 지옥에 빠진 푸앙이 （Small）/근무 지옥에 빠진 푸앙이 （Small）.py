N = int(input())
worker_time_table = {}
time_table = {0: 4, 1: 6, 2: 4, 3: 10}
is_fair = "Yes"
for _ in range(N):
    for t in range(4):
        workers = list(input().split())
        workers = [w for w in workers if w != '-']
        if not workers:
            break
        
        for w in workers:
            if w not in worker_time_table:
                worker_time_table[w] = time_table[t]
            else:
                worker_time_table[w] += time_table[t]
    
if worker_time_table:
    values = worker_time_table.values()
    max_time, min_time = max(values), min(values)
    if max_time - min_time > 12:
        is_fair = "No"

print(is_fair)