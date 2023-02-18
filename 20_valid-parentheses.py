class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if parentheses.get(c, False):
                if not len(stack):
                    return False
                top = stack.pop()
                close_parenthes = parentheses.get(c)
                if top != close_parenthes:
                    return False
                continue

            stack.append(c)

        if len(stack):
            return False
        return True

