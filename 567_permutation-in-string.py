from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = Counter(s1)
        count_s1_size = len(count_s1)
        count_s2 = Counter(s2[:len(s1)])
        left_letters = count_s1.copy()
        i = 0
        j = len(s1) - 1
        for k, v in count_s2.items():
            if k in left_letters:
                left_letters[k] = left_letters[k] - v
                if left_letters[k] == 0:
                    del left_letters[k]
        
        if len(left_letters) == 0:
                return True
        
        i += 1
        j += 1

        while j < len(s2):
            if s2[i-1] in count_s1:
                v = left_letters.get(s2[i-1], 0)
                left_letters[s2[i-1]] = left_letters[s2[i-1]] + 1
                if left_letters[s2[i-1]] == 0:
                    del left_letters[s2[i-1]]

            if len(left_letters) == 0:
                return True
            

            if s2[j] in count_s1:
                v = left_letters.get(s2[j], 0)
                left_letters[s2[j]] = left_letters[s2[j]] - 1
                if left_letters[s2[j]] == 0:
                    del left_letters[s2[j]]
            
            if len(left_letters) == 0:
                return True
            
            i += 1
            j += 1
        
        return False
            


if __name__ == "__main__":
    # s1 = "ab"
    # s2 = "eidbaooo"
    s1 = "abc"
    s2 = "cccccbabbbaaaa"
    print(Solution().checkInclusion(s1, s2))