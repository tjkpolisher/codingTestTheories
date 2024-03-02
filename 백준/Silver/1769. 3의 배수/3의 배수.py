X = input()
cnt = 0
while int(X) >= 10:
    X = sum([int(i) for i in X])
    X = str(X)
    cnt += 1

if int(X) % 3 == 0:
    answer = "YES"
else:
    answer = "NO"

print(cnt)
print(answer)