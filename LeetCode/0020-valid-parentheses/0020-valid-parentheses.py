class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_table = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c not in parentheses_table:
                stack.append(c)
            elif not stack or stack.pop() != parentheses_table[c]:
                return False
        return not stack
                
        