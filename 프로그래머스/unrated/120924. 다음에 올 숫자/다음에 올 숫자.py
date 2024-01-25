def solution(common):
    if common[1] - common[0] == common[2] - common[1]:
        d = common[1] - common[0]
        answer = common[-1] + d
    else:
        r = common[1] // common[0]
        answer = common[-1] * r
    return answer