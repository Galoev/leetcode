class Solution:
    def reverseString(self, s: List[str]) -> None:
        size = len(s)
        for i in range(size // 2):
            tmp = s[i]
            s[i] = s[size -1 - i]
            s[size - 1 - i] = tmp