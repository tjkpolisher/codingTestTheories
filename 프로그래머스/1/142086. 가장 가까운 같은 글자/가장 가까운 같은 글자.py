def solution(s):
    answer = []
    prev_index = []
    characters = []
    for i, c in enumerate(s):
        if c not in characters:
            answer.append(-1)
            prev_index.append(i)
            characters.append(c)
        else:
            answer.append(i - prev_index[characters.index(c)])
            prev_index[characters.index(c)] = i
    return answer