import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
sour = []
bitter = []

for _ in range(N):
    s, b = map(int, input().split())
    sour.append(s)
    bitter.append(b)


def recur(idx, s, b, use):
    global answer

    if idx == N:
        if not use:  # 아무 재료도 사용하지 않았다면 문제의 조건에 위배되므로 함수 종료
            return
        result = abs(s - b)
        answer = min(answer, result)
        return

    recur(idx + 1, s * sour[idx], b + bitter[idx], use + 1)
    recur(idx + 1, s, b, use)


answer = 10 ** 9
recur(0, 1, 0, 0)
print(answer)