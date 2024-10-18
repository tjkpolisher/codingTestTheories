from itertools import permutations
N, M = map(int, input().split())
N_list = list(range(1, N + 1))
p_list = list(permutations(N_list, M))
for p in p_list:
    print(*p)