def solution(n):
    # 점화식: a_n = a_{n-1} + a_{n-2} (a_1 = 1, a_2 = 2)
    ans = [0, 1, 2]
    for i in range(3, n + 1):
        ans.append((ans[i - 1] + ans[i - 2]) % 1234567)
    return ans[n]