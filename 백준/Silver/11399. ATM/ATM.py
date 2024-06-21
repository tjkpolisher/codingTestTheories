import sys
input = sys.stdin.readline

N = int(input())
p_list = list(map(int, input().split()))
p_list.sort()
mem = []
sum_n = 0
for p_i in p_list:
    p = p_i + sum_n
    mem.append(p)
    sum_n += p_i
print(sum(mem))