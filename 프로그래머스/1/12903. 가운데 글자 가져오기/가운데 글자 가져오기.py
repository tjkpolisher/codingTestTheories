def solution(s):
    length = len(s)
    if length % 2 == 0:
        half = length // 2 - 1
        answer = s[half:half + 2]
    else:
        half = length // 2
        answer = s[half]
    return answer