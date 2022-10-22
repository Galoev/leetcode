from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()

        for cur_str in strs:
            letter_count = [0] * 26
            for letter in cur_str:
                letter_count[ord(letter) - ord("a")] += 1

            anagrams = res.get(tuple(letter_count), [])
            if anagrams == []:
                res[tuple(letter_count)] = [cur_str]
            else:
                anagrams.append(cur_str)

        return res.values()


if __name__ == "__main__":
    # strs = ["eat","tea","tan","ate","nat","bat"]
    # strs = [""]
    strs = ["hhhhu","tttti","tttit","hhhuh","hhuhh","tittt"]
    print(Solution().groupAnagrams(strs))