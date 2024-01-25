def solution(nums):
    unique = len(set(nums))
    if len(nums) / 2 > unique:
        answer = unique
    else:
        answer = len(nums) / 2
    return answer