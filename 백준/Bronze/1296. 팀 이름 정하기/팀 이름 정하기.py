name = input()
love = list("LOVE")
counter_name = [name.count(love[i]) for i in range(4)]
answer = ''
N = int(input())
p = 0
for _ in range(N):
    team = input()
    counter = [counter_name[i] + team.count(love[i]) for i in range(4)]
    l, o, v, e = counter[0], counter[1], counter[2], counter[3]
    p_ = round(((l + o) * (l + v) * (l + e) * (o + v) * (o + e) * (v + e)) % 100, 5)
    
    if p < p_:
        p = p_
        answer = team
    elif p == p_:
        if not answer:
            answer = team
        elif answer > team:
            answer = team
print(answer)