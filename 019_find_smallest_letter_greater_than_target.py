from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1

        while left <= right:
            midle_idx = left + (right - left) // 2

            if letters[midle_idx] < target:
                left = midle_idx + 1
            else:
                right = midle_idx - 1

        return letters[left % len(letters)]

    
    # def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
    #     for letter in letters:
    #         if letter > target:
    #             return letter
        
    #     return letters[0]

s = Solution()
print(s.nextGreatestLetter(["c","f","j"], "a"))

