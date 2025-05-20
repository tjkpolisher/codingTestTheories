from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

ans = 0
permutations_list = permutations(A)
for perm in permutations_list:
    tmp = 0
    for i in range(N - 1):
        tmp += abs(perm[i] - perm[i + 1])
    ans = max(ans, tmp)

print(ans)