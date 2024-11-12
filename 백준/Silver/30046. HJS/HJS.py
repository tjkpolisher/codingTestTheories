import sys
input = sys.stdin.readline

N = int(input())
P = input().rstrip()
Q = input().rstrip()
R = input().rstrip()


def solution(N, P, Q, R):
    # P, Q, R 중 같은 문자열이 하나라도 있다면 Hmm... 출력
    if P == Q or Q == R or R == P:
        return "Hmm..."

    idx = 0
    # 공통 문자열 제거
    while idx < N and P[idx] == Q[idx] == R[idx]:
        idx += 1
    if idx == N:
        return "Hmm..."

    a, b, c = P[idx], Q[idx], R[idx]
    if a == b:
        if b != c:
            d, e = P, Q
        else:
            return "Hmm..."
    elif b == c:
        if a != b:
            d, e = Q, R
        else:
            return "Hmm..."
    elif a == c:
        return "Hmm..."
    else:
        return "HJS! HJS! HJS!"

    while idx < N and d[idx] == e[idx]:
        idx += 1
    if idx < N and d[idx] == c and e[idx] == a:
        return "Hmm..."
    else:
        return "HJS! HJS! HJS!"


print(solution(N, P, Q, R))