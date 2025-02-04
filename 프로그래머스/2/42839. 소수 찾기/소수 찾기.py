from math import sqrt
from itertools import permutations

def solution(numbers):
    answer = 0
    length = len(numbers)
    numbers = list(numbers)
    prime_number = set(range(2, 10 ** length))
    for i in range(2, int(sqrt(10 ** length)) + 1):
        prime_number -= set(range(2 * i, 10 ** length, i))
    
    seen_numbers = set()
    for i in range(1, length + 1):
        perms = permutations(numbers, i)
        perms = list(set(perms))
        for perm in perms:
            tmp = "".join(list(perm))
            tmp = int(tmp)
            if tmp in seen_numbers:
                continue
            if tmp in prime_number:
                answer += 1
                seen_numbers.add(tmp)
    
    return answer