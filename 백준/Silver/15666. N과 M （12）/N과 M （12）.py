import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
ans = []
ans_set = []


def answer(idx, ans):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(idx, N):
        if ans + [numbers[i]] in ans_set:
            continue
        ans_set.append(ans + [numbers[i]])
        answer(i, ans + [numbers[i]])
    return


answer(0, ans)