from copy import deepcopy
N, P = map(int, input().split())
numbers = []
x = deepcopy(N)
while True:
    x = (x * N) % P
    if x in numbers:
        break
    numbers.append(x)
print(len(numbers) - numbers.index(x))