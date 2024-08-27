import sys
input = sys.stdin.readline

N = int(input())
natural_numbers = list(map(int, input().split()))
natural_numbers.sort()

ans = 20000
diff = 20000 ** 2
for i in range(N):
    diff_cur = 0
    n = natural_numbers[i]
    for j in range(N):
        diff_cur += abs(n - natural_numbers[j])
        if diff_cur > diff:
            break
    if diff_cur > diff:
        continue
    if diff_cur == diff:
        diff = diff_cur
        ans = min(n, ans)
    elif diff_cur < diff:
        diff = diff_cur
        ans = n
print(ans)