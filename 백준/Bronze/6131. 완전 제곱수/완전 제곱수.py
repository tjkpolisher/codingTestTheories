N = int(input())
cnt = 0
nums = []

for i in range(1, round(N ** 0.5)):
    if N % i == 0:
        nums.append(i)
        
if len(nums) != 1:
    for num in nums:
        another_num = N // num
        for b in range(1, N + 1):
            for a in range(b + 1, N + 1):
                if a + b == another_num and a - b == num:
                    cnt += 1
print(cnt)