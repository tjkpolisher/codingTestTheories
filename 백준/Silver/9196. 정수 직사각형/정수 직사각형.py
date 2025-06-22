import sys
input = sys.stdin.readline

rectangles = []
for i in range(1, 151):
    for j in range(i + 1, 151):
        rectangles.append((i ** 2 + j ** 2, i, j))
rectangles.sort(key=lambda x: x[0])

idx = {(h, w): i for i, (_, h, w) in enumerate(rectangles)}

while True:
    test_case = input().rstrip()
    if test_case == '0 0':
        break
    h, w = map(int, test_case.split())
    i = idx[(h, w)]
    _, ans1, ans2 = rectangles[i + 1]
    print(ans1, ans2)