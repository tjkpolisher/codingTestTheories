def solution(number):
    from itertools import combinations
    combs = combinations(number, 3)
    answer = 0
    
    for comb in combs:
        if sum(comb) == 0:
            answer += 1
    return answer