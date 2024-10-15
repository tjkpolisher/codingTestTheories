N = input()
length = len(N)
slice1, slice2 = N[:length // 2], N[length // 2:]

sum1, sum2 = 0, 0
for i in range(length // 2):
    sum1 += int(slice1[i])
    sum2 += int(slice2[i])

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")