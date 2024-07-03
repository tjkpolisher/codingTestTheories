import sys
input = sys.stdin.readline

N, M = map(int, input().split())
number_list = list(map(int, input().split()))
prefix_sum = [0]

temp = 0
for n in number_list:
    temp += n
    prefix_sum.append(temp)

for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])