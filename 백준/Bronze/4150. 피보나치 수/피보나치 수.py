n = int(input())
f = []
for i in range(n):
    if i == 0 or i == 1:
        f.append(1)
    else:
        f_element = f[i - 2] + f[i - 1]
        f.append(f_element)
print(f[-1])