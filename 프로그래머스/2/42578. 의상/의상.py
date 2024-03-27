def solution(clothes):
    clothes_table = dict()
    for c in clothes:
        if c[1] not in clothes_table:
            clothes_table[c[1]] = ["", c[0]]
        else:
            clothes_table[c[1]].append(c[0])

    answer = 1
    for v in clothes_table.values():
        answer *= len(v)
    return answer - 1