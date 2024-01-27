import sys
input = sys.stdin.readline
N = int(input())
stack = []
original = []
for _ in range(N):
    original.append(int(input()))
m = original.index(max(original))
original = original[m:][::-1]
for i in range(len(original)):
    h = original[i]
    if not stack:
        stack.append(h)
    
    if (stack and stack[-1] < h):
        stack.append(h)
print(len(stack))