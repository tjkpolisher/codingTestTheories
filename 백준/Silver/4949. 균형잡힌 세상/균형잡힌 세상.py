import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == '.':
        break

    stack = []
    for c in string:
        if c in ("(", ")", "[", "]"):
            if not stack:
                stack.append(c)
                if c in (")", "]"):
                    break
            elif stack[-1] == "(" and c == ")":
                stack.pop()
            elif stack[-1] == "[" and c == "]":
                stack.pop()
            else:
                stack.append(c)
    if stack:
        print("no")
    else:
        print("yes")