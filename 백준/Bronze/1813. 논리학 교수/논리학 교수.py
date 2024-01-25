N = int(input())
ints = list(map(int, input().split()))

true = -1
for i in range(N + 1):
    counter = ints.count(i)
    if counter == i:
        true = max(true, i)
print(true)