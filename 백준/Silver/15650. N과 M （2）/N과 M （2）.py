N, M = map(int, input().split())
arr = []


def recur(number, output: list):
    if number == M:
        print(*output)
        return

    for i in range(1, N + 1):
        if i in output or (output and i < output[-1]):
            continue
        output.append(i)
        recur(number + 1, output)
        output.pop()  # 재귀 함수 종료 후 출력할 리스트를 원상 복구


recur(0, arr)