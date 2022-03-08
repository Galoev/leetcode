from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if not s:
            return [""]

        
        res = []
        if s[0].isdigit():
            for word in self.letterCasePermutation(s[1:]):
                res.append(f"{s[0]}{word}")
        else:
            for word in self.letterCasePermutation(s[1:]):
                res.append(f"{s[0].lower()}{word}")
                res.append(f"{s[0].upper()}{word}")
        
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.letterCasePermutation("a1b2"))