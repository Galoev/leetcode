# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        while l <= r and l <= n and r >= 0:
            i = l + (r - l) // 2
            if isBadVersion(i):
                r = i - 1
            else:
                l = i + 1
        
        if not isBadVersion(l):
            return l
        return r