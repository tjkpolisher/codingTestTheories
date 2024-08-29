def divide(lt, rt):
    if lt < rt:
        mid = (lt + rt) // 2

        divide(lt, mid)
        divide(mid + 1, rt)

        p1 = lt
        p2 = mid + 1
        p3 = lt

        while p1 <= mid and p2 <= rt:
            if arr[p1] < arr[p2]:
                tmp[p3] = arr[p1]
                p1 += 1
            else:
                tmp[p3] = arr[p2]
                p2 += 1
            p3 += 1

        while p1 <= mid:
            tmp[p3] = arr[p1]
            p1 += 1
            p3 += 1

        while p2 <= rt:
            tmp[p3] = arr[p2]
            p2 += 1
            p3 += 1

        for i in range(lt, rt + 1):
            arr[i] = tmp[i]


# 메인 함수 부분
n = int(input())  # 예시: 5

arr = list(map(int, input().split()))  # 예시: 4 1 3 9 7
tmp = [0] * n

divide(0, n - 1)

for i in range(n):
    print(arr[i], end=" ")
