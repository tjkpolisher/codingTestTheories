def solution(n, lost, reserve):
    lost_new = list(set(lost) - set(reserve))
    reserve_new = list(set(reserve) - set(lost))
    answer = len(lost_new)
    for r in reserve_new:
        if r - 1 in lost_new:
            lost_new.remove(r - 1)
            answer -= 1
        elif r + 1 in lost_new:
            lost_new.remove(r + 1)
            answer -= 1
    answer = n - answer
    return answer