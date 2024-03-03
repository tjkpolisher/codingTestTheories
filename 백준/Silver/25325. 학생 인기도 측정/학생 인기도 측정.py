n = int(input())
names = list(input().split())
d = {name: 0 for name in names}

for _ in range(n):
    like_name = list(input().split())
    for n in like_name:
        d[n] += 1

for name, value in sorted(d.items(), key=lambda item: item[1], reverse=True):
    print(name, value)