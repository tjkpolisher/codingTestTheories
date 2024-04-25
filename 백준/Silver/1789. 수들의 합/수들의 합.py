S = int(input())
total = 0
cnt = 0

while total <= S:
    cnt += 1
    total += cnt

print(cnt - 1)