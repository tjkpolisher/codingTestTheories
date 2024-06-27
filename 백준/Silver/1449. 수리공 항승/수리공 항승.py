import sys
input = sys.stdin.readline

N, L = map(int, input().split())
leaks = list(map(int, input().split()))
leaks.sort()

cnt = 0
is_tape = [False] * (leaks[-1] + 1)  # 테이프를 붙였는지 여부를 판단
for pos in leaks:
    # print(f"{pos=}")
    # print(f"{is_tape[pos]=}")
    if not is_tape[pos]:
        for i in range(pos, min(leaks[-1] + 1, pos + L)):
            is_tape[i] = True
        cnt += 1
        # print(f"{cnt=}")
        # print(f"{is_tape=}")
print(cnt)