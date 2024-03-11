import math
N_list = list(map(int, input()))
nums = dict()
for n in N_list:
    if n not in nums:
        nums[n] = 1
    else:
        nums[n] += 1

if 6 in nums and 9 in nums:
    nums[6] += nums[9]
    del nums[9]
    nums[6] = math.ceil(nums[6] / 2)
elif 6 in nums:
    nums[6] = math.ceil(nums[6] / 2)
elif 9 in nums:
    nums[9] = math.ceil(nums[9] / 2)

print(max(nums.values()))