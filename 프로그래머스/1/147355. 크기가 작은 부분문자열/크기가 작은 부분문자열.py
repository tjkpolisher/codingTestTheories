def solution(t, p):
    answer = 0
    for i in range(len(t) - len(p) + 1):
        is_small = (t[i:i+len(p)] <= p)
        if is_small:
            answer += 1
    return answer