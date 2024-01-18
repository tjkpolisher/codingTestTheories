def solution(nums):
    from itertools import combinations
    nums = sorted(nums)
    answer = 0
    combs = list(combinations(nums, 3))
    summations = [sum(list(comb)) for comb in combs]
    prime_numbers = prime_number(sum(nums[-3:]))
    for s in summations:
        if s in prime_numbers:
            answer += 1

    return answer

def prime_number(n):
    p = set(range(2, n + 1))
    for i in range(2, n + 1):
        p -= set(range(2 * i, n + 1, i))
    
    return list(p)