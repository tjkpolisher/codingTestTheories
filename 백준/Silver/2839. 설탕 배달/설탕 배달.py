N = int(input())
five = N // 5
ans = []
for i in range(five + 1):
    rem = N - 5 * i
    if rem % 3 == 0:
        ans.append(i + rem // 3)

if not ans:
    print(-1)
else:
    print(min(ans))