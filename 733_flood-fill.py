from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        origColor = None
        if color == image[sr][sc]:
            origColor = color
            color = -1
            flag = True
        origVal = image[sr][sc]
        image[sr][sc] = color

        if sr - 1 >= 0 and image[sr - 1][sc] == origVal:
            self.helper(image, sr-1, sc, color, origVal)
        if sr + 1 < len(image) and image[sr + 1][sc] == origVal:
            self.helper(image, sr + 1, sc, color, origVal)
        if sc - 1 >= 0 and image[sr][sc - 1] == origVal:
            self.helper(image, sr, sc - 1, color, origVal)
        if sc + 1 < len(image[0]) and image[sr][sc + 1] == origVal:
            self.helper(image, sr, sc + 1, color, origVal)
        
        if origColor != None:
            for row in range(len(image)):
                for col in range(len(image[0])):
                    if image[row][col] == -1:
                        image[row][col] = origColor
        
        return image

    
    def helper(self, image: List[List[int]], sr: int, sc: int, color: int, origVal: int):
        image[sr][sc] = color

        if sr - 1 >= 0 and image[sr - 1][sc] == origVal:
            self.helper(image, sr-1, sc, color, origVal)
        if sr + 1 < len(image) and image[sr + 1][sc] == origVal:
            self.helper(image, sr + 1, sc, color, origVal)
        if sc - 1 >= 0 and image[sr][sc - 1] == origVal:
            self.helper(image, sr, sc - 1, color, origVal)
        if sc + 1 < len(image[0]) and image[sr][sc + 1] == origVal:
            self.helper(image, sr, sc + 1, color, origVal)


if __name__ == "__main__":
    s = Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2
    print(s.floodFill(image, sr, sc, color))