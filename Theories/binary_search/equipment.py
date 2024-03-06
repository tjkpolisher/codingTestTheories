import sys
input = sys.stdin.readline


def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


N = int(input())
stored = list(map(int, input().split()))
stored.sort()

M = int(input())
requested = list(map(int, input().split()))

for r in requested:
    result = binary_search(stored, r, 0, N - 1)
    if not result:
        print("no", end=' ')
    else:
        print("yes", end=' ')
