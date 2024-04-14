from math import factorial
N = int(input())
if N <= 4:
    print(0)
else:
    f = str(factorial(N))
    length = len(f)
    f_flipped = str(int(f[::-1]))
    length_f = len(f_flipped)
    print(length - length_f)