def solution(s):
    s = s.lower()
    p_counter = s.count('p')
    y_counter = s.count('y')
    if p_counter == y_counter:
        answer = True
    else:
        answer = False

    return answer