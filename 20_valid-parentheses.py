class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if parentheses.get(c, False):
                top = stack.pop()
                close_parenthes = parentheses.get(c)
                if top != close_parenthes:
                    return False
                continue

            stack.append(c)

        
        return True

