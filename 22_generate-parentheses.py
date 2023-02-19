from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur_parenthesis = []
        max_parenthesis = 2 * n
        def genereate(parenthe: str, open: int, close: int):
            cur_parenthesis.append(parenthe)

            if open < close:
                return
            if open > n:
                return

            if open + close == max_parenthesis:
                res.append("".join(cur_parenthesis))
                return

            genereate(')', open, close+1)
            cur_parenthesis.pop()
            genereate('(', open+1, close)
            cur_parenthesis.pop()
        
        genereate('(', 1, 0)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))

        
