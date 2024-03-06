N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

for n in sorted(nums):
    print(n)