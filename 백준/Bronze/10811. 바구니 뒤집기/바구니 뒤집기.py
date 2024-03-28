N, M = map(int, input().split())
array = list(range(1, N + 1))
for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    if i != 0 and j != N - 1:
        array = array[:i] + array[i:j + 1][::-1] + array[j + 1:]
    elif i == 0:
        array = array[:j + 1][::-1] + array[j + 1:]
    elif j == N - 1:
        array = array[:i] + array[i:][::-1]
print(*array, end=' ')