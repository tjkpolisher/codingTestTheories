import sys
input = sys.stdin.readline

N = int(input())
room = []
for _ in range(N):
    room.append(list(input().rstrip()))

ans = [0, 0]  # 가로일 때의 답, 세로일 때의 답
for i in range(N):
    r, c = 0, 0
    for j in range(N):
        if room[i][j] == '.':
            r += 1
        else:
            r = 0
        if r == 2:
            ans[0] += 1

        if room[j][i] == '.':
            c += 1
        else:
            c = 0
        if c == 2:
            ans[1] += 1

print(ans[0], ans[1])