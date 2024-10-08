def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


def solution(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        gcd_temp = gcd(arr[i], ans)
        ans = gcd_temp * (arr[i] // gcd_temp) * (ans // gcd_temp)
    return ans