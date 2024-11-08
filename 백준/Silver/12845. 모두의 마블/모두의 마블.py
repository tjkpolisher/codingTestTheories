n = int(input())
levels = list(map(int, input().split()))

levels.sort(reverse=True)
level_0 = levels[0]

golds = 0
for i in range(1, n):
    golds += level_0 + levels[i]
    if level_0 < levels[i]:
        level_0 = levels[i]

print(golds)