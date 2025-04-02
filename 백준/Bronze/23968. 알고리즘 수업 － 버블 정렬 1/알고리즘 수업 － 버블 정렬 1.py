N, K = map(int, input().split())
A = list(map(int, input().split()))

if N ** 2 < K:
    print(-1)
    exit()


def bubble_sort(arr, k):
    cnt = 0
    for i in range(N, 0, -1):
        for j in range(0, i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                cnt += 1
            if cnt == k:
                return f'{arr[j]} {arr[j + 1]}'
    return -1


print(bubble_sort(A, K))