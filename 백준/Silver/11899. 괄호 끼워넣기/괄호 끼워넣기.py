S = input()
stack = []
for ch in S:
    if not stack:
        stack.append(ch)
    elif stack[-1] == '(' and ch == ')':
        stack.pop()
    else:
        stack.append(ch)

print(len(stack))