M = int(input())
N = int(input())
squared = [i ** 2 for i in range(1, 101)]
ans = []
for i in range(M, N + 1):
    if i in squared:
        ans.append(i)
if not ans:
    print(-1)
else:
    print(sum(ans))
    print(min(ans))