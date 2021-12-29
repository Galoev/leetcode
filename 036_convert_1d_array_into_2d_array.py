from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != (m*n):
            return []

        array_2d = []
        for i in range(m):
            array_2d.append(original[n*i:n*(i+1)])
        return array_2d

if __name__ == "__main__":
    s = Solution()
    print(s.construct2DArray(original = [1,2,3,4], m = 2, n = 2))