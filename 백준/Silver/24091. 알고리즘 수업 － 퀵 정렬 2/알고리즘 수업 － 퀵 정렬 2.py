import sys
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))


def quicksort(array, p, r):
    if p < r:
        q = partition(array, p, r)  # 분할
        quicksort(array, p, q - 1)  # 왼쪽 부분 배열 정렬
        quicksort(array, q + 1, r)  # 오른쪽 부분 배열 정렬


def partition(array, p, r):
    x = array[r]  # 피봇 원소
    i = p - 1  # x보다 작거나 같은 원소들의 끝 지점
    for j in range(p, r):
        if array[j] <= x:
            # i 값 증가 후 A[i]와 A[j] 교환
            i += 1
            swap(array, i, j)
    if i + 1 != r:
        swap(array, i + 1, r)
    return i + 1


def swap(array, i, j):
    global cnt
    cnt += 1
    array[i], array[j] = array[j], array[i]
    if cnt == K:
        print(*array)
        exit()


cnt = 0  # 교환 횟수를 저장할 변수
quicksort(A, 0, N - 1)
print(-1)  # 정렬 횟수를 다 채우지 못하고 도중에 종료되지 않으면 -1 출력