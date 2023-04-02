class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            if not (s[l].isalpha() or s[l].isnumeric()):
                l += 1
                continue
            if not (s[r].isalpha() or s[r].isnumeric()):
                r -= 1
                continue
            
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        
        return True
    

if __name__ == "__main__":
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))