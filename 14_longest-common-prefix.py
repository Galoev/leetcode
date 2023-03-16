from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = -1
        flag = True
        while flag:
            i += 1
            if i >= len(strs[0]):
                return str
            cur_char = strs[0][i]
            for str in strs:
                if i >= len(str):
                    return str
                if str[i] != cur_char:
                    if i == 0:
                        return ""
                    flag = False
                    break
        
        return strs[0][0:i]


if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))