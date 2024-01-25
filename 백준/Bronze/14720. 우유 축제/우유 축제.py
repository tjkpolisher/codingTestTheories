N = int(input())
milk = list(map(int, input().split()))
d = []
for i, m in enumerate(milk):
    idx = len(d) % 3
    if m == idx:
        d.append(m)
print(len(d))