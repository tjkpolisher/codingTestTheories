T = int(input())

for i in range(T):
    dictionary = {}
    res = 0
    n, L, F = map(int, input().split())
    arr = list(input().split())

    for j in arr:
        tmp = j[-F:]
        if tmp in dictionary:
            dictionary[tmp] += 1
        else:
            dictionary[tmp] = 1

    for j in dictionary:
        if dictionary[j] > 1:
            res += dictionary[j] // 2
    print(res)