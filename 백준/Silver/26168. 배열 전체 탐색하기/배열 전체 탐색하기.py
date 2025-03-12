import sys
import bisect
input = sys.stdin.readline

n, m = map(int, input().split())
A = sorted(list(map(int, input().split())))

for _ in range(m):
    query = input().rstrip().split()
    qtype = query[0]

    if qtype == "1":
        k = int(query[1])
        result = n - bisect.bisect_right(A, k - 1)
    elif qtype == "2":
        k = int(query[1])
        result = n - bisect.bisect_right(A, k)
    else:
        i = int(query[1])
        j = int(query[2])
        result = bisect.bisect_right(A, j) - bisect.bisect_left(A, i)

    print(result)