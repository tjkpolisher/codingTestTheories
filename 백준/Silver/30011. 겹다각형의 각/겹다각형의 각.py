N = int(input())
vertex = list(map(int, input().split()))


def solution(N, vertex):
    if N == 1:
        angle = 180 * (vertex[0] - 2)
    else:
        angle = 0
        for i in range(N):
            angle += 180 * (vertex[i] - 2)
            if i < N - 1:
                angle += 180 * vertex[i + 1] - 180 * (vertex[i + 1] - 2)
    return angle


print(solution(N, vertex))