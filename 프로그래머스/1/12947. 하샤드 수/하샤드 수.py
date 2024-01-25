def solution(x):
    l = list(str(x))
    nums = [int(l[i]) for i in range(len(l))]
    answer = True if x % sum(nums) == 0 else False
    return answer