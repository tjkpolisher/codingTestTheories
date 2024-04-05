import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().rstrip().split()))  # 잉크지수
b = list(map(int, input().rstrip().split()))  # 점도지수
result = []


for i in range(N):
    idx = a[i]
    start, end = i + 1, N - 1
    ans = i
    while start <= end:
        mid = (start + end) // 2
        if idx < b[mid]:
            end = mid - 1
        else:
            start = mid + 1
            ans = mid
    result.append(str(ans - i))

print(' '.join(result))