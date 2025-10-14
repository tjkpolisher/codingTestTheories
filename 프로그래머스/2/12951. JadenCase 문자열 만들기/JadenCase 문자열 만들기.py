def solution(s):
    answer = []
    is_first = True
    for i, ch in enumerate(s):
        if ch == " ":
            answer.append(ch)
            is_first = True
        elif 65 <= ord(ch) <= 122:
            if is_first:
                answer.append(ch.upper())
                is_first = False
            else:
                answer.append(ch.lower())
        else:
            answer.append(ch)
            is_first = False
    return ''.join(answer)