def solution(n, m, section):
    from collections import deque
    section = deque(section)
    answer = 0

    while section:
        start_point = section[0]
        end_point = start_point + m

        while section and section[0] < end_point:
            section.popleft()

        answer += 1

    return answer