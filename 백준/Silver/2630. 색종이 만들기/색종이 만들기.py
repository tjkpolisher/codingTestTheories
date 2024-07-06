import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

n_white = 0
n_blue = 0


def slice(x, y, n):
    global n_white, n_blue

    color = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                slice(x, y, n // 2)
                slice(x, y + n // 2, n // 2)
                slice(x + n // 2, y, n // 2)
                slice(x + n // 2, y + n // 2, n // 2)
                return

    if color == 0:
        n_white += 1
    else:
        n_blue += 1


slice(0, 0, N)

print(n_white)
print(n_blue)