import sys
input = sys.stdin.readline

S = input().rstrip()
cnt = 0

for i in range(1, len(S)):
    if S[i - 1] != S[i]:
        cnt += 1

print((cnt + 1) // 2)