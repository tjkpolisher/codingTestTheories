def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)
    
    allowed = []
    for schedule in schedules:
        h, m = divmod(schedule, 100)
        allowed.append(h * 60 + m + 10)
    
    for i in range(n):
        ok = True
        for j in range(7):
            dow = (startday - 1 + j) % 7
            if dow <= 4:
                t = timelogs[i][j]
                th, tm = divmod(t, 100)
                t_min = th * 60 + tm
                if t_min > allowed[i]:
                    ok = False
                    break
        if ok:
            answer += 1
    
    return answer