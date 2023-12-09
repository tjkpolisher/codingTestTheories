def solution(dots):
    xs = []
    ys = []
    for i in range(len(dots)):
        if dots[i][0] not in xs:
            xs.append(dots[i][0])
        if dots[i][1] not in ys:
            ys.append(dots[i][1])
        
        if len(xs)==2 and len(ys)==2:
            break
    answer = abs(xs[1] - xs[0]) * abs(ys[1] - ys[0])
    return answer