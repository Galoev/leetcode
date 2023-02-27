class Solution:
    def skipSymbols(self, s: str, i: int) -> int:
        skip = 0
        while i >= 0:
            if s[i] == '#':
                skip += 1
                i -= 1
            elif skip > 0:
                skip -= 1
                i -= 1
            else:
                break
        return i

    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        
        while i >= 0 and j >= 0:
            if s[i] == '#':
                i = self.skipSymbols(s, i)
            if t[j] == '#':
                j = self.skipSymbols(t, j)
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False

            i -= 1
            j -= 1
        if i >= 0 and s[i] == '#':
            i = self.skipSymbols(s, i)
        if j >= 0 and t[j] == '#':
            j = self.skipSymbols(t, j)
        
        if i == j:
            return True
        
        if i >= -1 or j >= -1:
            return False
        
        return True


if __name__ == "__main__":
    sol = Solution()
    # s = "ab#c"
    # t = "ad#c"
    # s = "ab##"
    # t = "c#d#"
    s = "a#c"
    t = "b" # false
    # s = "bxj##tw"
    # t = "bxo#j##tw"
    # s = "j##xfix"
    # t = "j###xfix"
    # s = "bbbextm"
    # t = "bbb#extm"
    # s = "nzp#o#g"
    # t = "b#nzp#o#g"
    # s = "aaa###a"
    # t = "aaaa###a"
    # s = "a##cab##"
    # t = "a##c" #true
    print(sol.backspaceCompare(s, t))