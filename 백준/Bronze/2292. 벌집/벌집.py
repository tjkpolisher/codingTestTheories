N = int(input())

n = 1
counter = 1
while N > n:
    n += 6 * counter
    counter += 1
print(counter)