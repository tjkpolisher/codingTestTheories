N, r, c = map(int, input().split())


def solution(N, r, c):
    if not N:
        return 0
    return 2 * (r % 2) + (c % 2) + 4 * solution(N - 1, int(r / 2), int(c / 2))


print(solution(N, r, c))