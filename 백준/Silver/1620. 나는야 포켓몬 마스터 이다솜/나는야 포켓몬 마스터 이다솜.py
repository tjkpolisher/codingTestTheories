import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
p_n = dict()
n_p = dict()

for i in range(N):
    p = input().rstrip()
    n = i + 1
    p_n[p] = n
    n_p[n] = p

for _ in range(M):
    prob = input().rstrip()
    # 문제가 숫자일 경우
    try:
        prob = int(prob)
        print(n_p[prob])
    except ValueError:
        print(p_n[prob])