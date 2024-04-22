K = int(input())
stack = []
for _ in range(K):
    n = int(input())
    if n != 0:
        stack.append(n)
    elif n == 0:
        stack.pop()
print(sum(stack))