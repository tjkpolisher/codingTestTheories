def solution(k, score):
    answer = []
    hof = []
    for idx, s in enumerate(score):
        hof.append(s)
        hof = sorted(hof, reverse = True)
        if len(hof) > k:
            hof = hof[:k]
        answer.append(min(hof))
    return answer