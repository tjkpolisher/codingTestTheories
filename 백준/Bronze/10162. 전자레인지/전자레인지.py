T = int(input())
A, r = divmod(T, 300)
B, r = divmod(r, 60)
C, r = divmod(r, 10)
if r != 0:
    print(-1)
else:
    print(A, B, C)