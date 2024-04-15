import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
A.sort()
M = int(input().rstrip())
Ms = list(map(int, input().rstrip().split()))


def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == target:
            return 1
        elif A[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


for i in range(M):
    target = Ms[i]
    print(binary_search(0, N - 1, target))