formula = input()
parsed = list(formula.split('-'))
ans = 0
for i in range(len(parsed)):
    tmp = 0
    c = parsed[i].split('+')
    for j in range(len(c)):
        tmp += int(c[j])
    if i == 0:
        ans = tmp
    else:
        ans -= tmp
print(ans)