N = int(input())
A = list(map(int, input().split()))
NGE = [0] * N
stack = []

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        NGE[stack.pop()] = A[i]
    stack.append(i)

while stack:
    NGE[stack.pop()] = -1

print(*NGE)