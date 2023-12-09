def solution(spell, dic):
    answer = 2
    for word in dic:
        counter = 0
        for c in spell:
            if c in word:
                counter += 1
        if counter == len(spell):
            answer = 1
            break
    return answer