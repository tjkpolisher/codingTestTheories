N = int(input())
matrix = []
diag1 = 0
diag2 = 0
nums = set()
sum_result = N * (N ** 2 + 1) // 2
broken = False

for i in range(N):
    N_i = list(map(int, input().split()))
    if sum(N_i) != sum_result:
        broken = True
    for num in N_i:
        if num < 1 or num > N ** 2 or num in nums:
            broken = True
        nums.add(num)
    matrix.append(N_i)
    diag1 += N_i[i]
    diag2 += N_i[N - i - 1]

for i in range(N):
    vertical_sum = 0
    for j in range(N):
        vertical_sum += matrix[i][j]
    if vertical_sum != sum_result:
        broken = True

if broken or diag1 != sum_result or diag2 != sum_result:
    print("FALSE")
else:
    print("TRUE")