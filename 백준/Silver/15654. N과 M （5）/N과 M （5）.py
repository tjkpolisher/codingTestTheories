import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sequence = list(map(int, input().split()))

sequence.sort()
answer = []


def backtrack():
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return

    for i in range(N):
        next = sequence[i]
        if next in answer:
            continue
        answer.append(next)
        backtrack()
        answer.pop()


backtrack()