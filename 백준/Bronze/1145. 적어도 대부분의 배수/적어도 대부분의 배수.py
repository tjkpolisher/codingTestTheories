import math
from itertools import combinations

def lcm(a, b):
    return int(a * b / math.gcd(a, b))

nums = list(map(int, input().split()))
nums.sort()

answers = []
combs = combinations(nums, 3)
for comb in combs:
    answers.append(lcm(lcm(comb[0], comb[1]), comb[2]))
print(min(answers))