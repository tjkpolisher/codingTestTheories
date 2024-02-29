N = int(input())
K = int(input())
prime_factors = set(range(2, N + 1))

for i in range(2, N + 1):
    multiple = set(range(2 * i, N + 1, i))
    prime_factors -= multiple

nums = [1] * (N + 1)
for i in range(2, N + 1):
    if i in prime_factors and i > K:
        for j in range(i, N + 1, i):
            nums[j] = 0

print(sum(nums) - 1)