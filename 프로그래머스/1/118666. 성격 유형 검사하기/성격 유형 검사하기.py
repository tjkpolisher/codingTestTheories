def solution(survey, choices):
    answer = ''
    scoreboard = {'R': 0, 'T': 0, 'C': 0, 'F': 0,
                  'J': 0, 'M': 0, 'A': 0, 'N': 0}
    length = len(survey)

    for i in range(length):
        s = survey[i]
        c = choices[i]
        if c == 4:
            continue
        elif c > 4:
            scoreboard[s[1]] += (c - 4)
        else:
            scoreboard[s[0]] += (4 - c)

    if scoreboard['R'] >= scoreboard['T']:
        answer += 'R'
    else:
        answer += 'T'
    if scoreboard['C'] >= scoreboard['F']:
        answer += 'C'
    else:
        answer += 'F'
    if scoreboard['J'] >= scoreboard['M']:
        answer += 'J'
    else:
        answer += 'M'
    if scoreboard['A'] >= scoreboard['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer