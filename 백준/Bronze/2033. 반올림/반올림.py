import math
N = int(input())
try:
    j = int(math.log10(N)) + 1 # N의 자릿수
    for i in range(1, j):
        if int(str(N)[-i]) == 5:
            N = N + (10 ** (i-1)) * 5
        else:
            N = round(N, -i)
except ValueError:
    pass
print(N)