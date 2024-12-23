N = int(input())
if N == 0:
    print("NO")
    exit(0)

exponent = 1  # 3의 거듭제곱의 지수
while 3 ** exponent <= N:
    exponent += 1
exponent -= 1

while True:
    c = int(3 ** exponent)
    if c <= N:
        N -= c
    exponent -= 1
    if exponent < 0 or N <= 0:
        break

if N:
    print("NO")
else:
    print("YES")