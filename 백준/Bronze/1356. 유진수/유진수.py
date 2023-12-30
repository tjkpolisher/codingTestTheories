def product(l):
    a = 1
    for i in range(len(l)):
        a *= int(l[i]) 
    return a

N = input()
answer = 'NO'
if len(N) == 1:
    pass
else:
    for i in range(1, len(N)):
        front, end = list(N[:i]), list(N[i:])
        front_mul, end_mul = product(front), product(end)
        if front_mul == end_mul:
            answer = 'YES'
            break
print(answer)