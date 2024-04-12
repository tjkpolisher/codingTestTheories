def solution(s):
    stack = []
    for c in s:
        if not stack and (c == ')' or c == '}' or c == ']'):
            return False
        elif c == '(' or c == '{' or c == '[':
            stack.append(c)
        elif stack[-1] == '(' and c == ')':
            stack.pop()
        elif stack[-1] == '{' and c == '}':
            stack.pop()
        elif stack[-1] == '[' and c == ']':
            stack.pop()
        
    
    return True if not stack else False