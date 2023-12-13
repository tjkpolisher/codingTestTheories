A, B = map(int, input().split())
array = []
for i in range(1, 48):
    for j in range(i):
        array.append(i)
print(sum(array[A-1:B]))