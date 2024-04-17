def parentheses(string):
    stack = []
    for c in string:
        if not stack:
            if c == ")":
                return "NO"
            else:
                stack.append(c)
        elif stack[-1] == "(" and c == ")":
            stack.pop()
        else:
            stack.append(c)
    if not stack:
        return "YES"
    else:
        return "NO"


T = int(input())
for _ in range(T):
    string = input()
    print(parentheses(string))