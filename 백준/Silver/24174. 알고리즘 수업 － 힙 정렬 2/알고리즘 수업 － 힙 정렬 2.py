import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

A = [0] + arr

cnt = 0
found = False


def heapify(A, k, n):
    global cnt, K, found
    
    left = 2 * k
    right = 2 * k + 1
    
    if right <= n:
        if A[left] < A[right]:
            smaller = left
        else:
            smaller = right
    elif left <= n:
        smaller = left
    else:
        return
    
    if A[smaller] < A[k]:
        A[smaller], A[k] = A[k], A[smaller]
        cnt += 1
        if cnt == K:
            print(*A[1:])
            found = True
            return

        heapify(A, smaller, n)


def build_min_heap(A, n):
    for i in range(n // 2, 0, -1):
        if found:
            return
        heapify(A, i, n)


def heap_sort(A, n):
    global cnt, found

    build_min_heap(A, n)

    for i in range(n, 1, -1):
        if found:
            return

        A[1], A[i] = A[i], A[1]
        cnt += 1

        if cnt == K:
            print(*A[1:])
            found = True
            return

        heapify(A, 1, i - 1)


heap_sort(A, N)
if not found:
    print(-1)