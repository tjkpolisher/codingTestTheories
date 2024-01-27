def solution(s):
    # 괄호 짝 맞추기
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                return False
            else:
                stack.pop()
    
    if len(stack) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    ex1 = "(())()"
    ex2 = "((())()"
    for e in [ex1, ex2]:
        print(solution(e))