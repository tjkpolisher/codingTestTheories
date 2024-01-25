def solution(d, budget):
    answer = 0
    d = sorted(d)
    for d_ in d:
        if budget - d_ >= 0:
            answer += 1
            budget -= d_
        else:
            break
    return answer