from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        pairs = dict()
        same_letters = dict()
        for word in words:
            if word[0] == word[1]:
                count = same_letters.get(word, 0)
                same_letters[word] = count + 1
                continue
            
            if not pairs.get(word):
                pairs[f"{word[1]}{word[0]}"] = pairs.get(f"{word[1]}{word[0]}", 0) + 1
                continue
            
            res += 4
            pairs[word] = pairs[word] - 1
            if pairs[word] == 0:
                del pairs[word]
        
        flag_odd_count_same_letters = False
        for k, v in same_letters.items():
            if v % 2 == 1:
                flag_odd_count_same_letters = True
                res += (v - 1) * 2
                continue
                
            res += v * 2
        
        if flag_odd_count_same_letters:
            res += 2


        return res
            

if __name__ == "__main__":
    # words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
    words = ["qo","fo","fq","qf","fo","ff","qq","qf","of","of","oo","of","of","qf","qf","of"]
    print(Solution().longestPalindrome(words))

# "qo",
# "fo","of",
# "fo","of",
# "fq","qf",
# "ff",
# "qq",
# "qf",
# "oo",
# "of",
# "of",
# "qf",
# "qf",
# "of"
