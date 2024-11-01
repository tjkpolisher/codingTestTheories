from itertools import product

c = int(input())

sevens = [1]
e = 1
while 7 ** e <= c:
    sevens.append(7 ** e)
    e += 1
sevens = sevens[::-1]

exponents = [2, 1, 0]
combs = list(product(exponents, repeat=len(sevens)))

ans = 0
for idx, comb in enumerate(combs):
    summation = 0
    c_list = list(comb)
    for i in range(len(c_list)):
        summation += sevens[i] * c_list[i]

    if summation == c:
        ans = len(combs) - idx - 1
        break

print(ans)