n = int(input())


def solve(n):
    total = (n * (n - 1)) // 2
    target = (total + 1) // 2

    left, right = 1, n - 1
    ans = n - 1

    while left <= right:
        mid = (left + right) // 2
        comparisons = mid * n - (mid * (mid + 1)) // 2

        if comparisons >= target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


print(solve(n))