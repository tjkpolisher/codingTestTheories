import sys
input = sys.stdin.readline

N = int(input())
name_and_A = []
for _ in range(N):
    name, jaehak, icpc, S, A = input().rstrip().split()
    S, A = int(S), int(A)
    if jaehak == 'hewhak':
        continue
    if icpc == 'winner':
        continue
    if S <= 3 and S != -1:
        continue
    name_and_A.append([name, A])

name_and_A.sort(key=lambda x: x[1])
answer = name_and_A[:10]
print(len(answer))
answer.sort(key=lambda x: x[0])
for ans in answer:
    print(ans[0])