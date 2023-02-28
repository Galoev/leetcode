class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = dict()
        max_len = 0
        cur_len = 0
        i = 0
        while i < len(s):
            c = s[i]
            if c not in letters:
                letters[c] = i
                cur_len += 1
                i += 1
            else:
                max_len = max(max_len, cur_len)
                i = letters[c] + 1 
                letters = dict()
                cur_len = 0
        
        return max(max_len, cur_len)


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))