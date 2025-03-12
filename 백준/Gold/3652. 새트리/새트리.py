import sys
sys.setrecursionlimit(10 ** 6)

a, b = map(int, input().split('/'))


def bird(a, b):
    if a == 1 and b == 1:
        return
    if a > b:
        print("R", end="")
        bird(b, a - b)
    else:
        print("L", end="")
        bird(b - a, a)


bird(a, b)