import sys
input = sys.stdin.readline

N = int(input())
numbers = []
numbers_table = dict()
for _ in range(N):
    n = int(input())
    numbers.append(n)
    if n not in numbers_table:
        numbers_table[n] = 1
    else:
        numbers_table[n] += 1

numbers = sorted(numbers)
# 산술 평균
print(int(round(sum(numbers) / N)))
# 중앙값
print(numbers[N // 2])
# 최빈값
f = max(numbers_table.values())
f_list = []
for i in numbers_table:
    if f == numbers_table[i]:
        f_list.append(i)
f_list.sort()
if len(f_list) > 1:
    print(f_list[1])
else:
    print(f_list[0])
# 범위
print(numbers[-1] - numbers[0])