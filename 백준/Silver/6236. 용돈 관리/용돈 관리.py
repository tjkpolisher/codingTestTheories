import sys
input = sys.stdin.readline


def withdraw_check(k, m, amounts):
    cnt = 1
    current_sum = 0

    for amount in amounts:
        if current_sum + amount > k:
            cnt += 1
            current_sum = 0

        current_sum += amount

    return cnt <= m


N, M = map(int, input().split())
amounts = [int(input()) for _ in range(N)]

left, right = max(amounts), sum(amounts)
ans = right

while left <= right:
    mid = (left + right) // 2
    if withdraw_check(mid, M, amounts):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)