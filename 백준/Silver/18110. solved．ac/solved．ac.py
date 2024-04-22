import sys
input = sys.stdin.readline


def new_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


n = int(input().rstrip())
if not n:
    print(0)
else:
    opinion = []
    cut = new_round(n * 0.15)
    for _ in range(n):
        opinion.append(int(input().rstrip()))

    opinion.sort()
    if cut:
        print(new_round(sum(opinion[cut:-cut]) / (n - 2 * cut)))
    else:
        print(new_round(sum(opinion) / (n - 2 * cut)))