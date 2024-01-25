scores = []
for _ in range(10):
    n = int(input())
    scores.append(n)

opt = 0
for i in range(10):
    s = sum(scores[:i+1])
    if abs(100 - s) < abs(100 - opt) or (abs(100 - s) == abs(100 - opt) and s > opt):
        opt = s
print(opt)