from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters_count = Counter(s)
        res = 0
        odd = False
        for v in letters_count.values():
            if v % 2 == 0:
                res += v
            else:
                res += v - 1
                odd = True
            
        return res + 1 if odd else res