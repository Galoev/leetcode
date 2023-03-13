from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num += 1
                    self.markIsland(grid, i, j)
        
        return num
    
    def markIsland(self, grid: List[List[str]], y: int, x: int):
        grid[y][x] = -1
        if y - 1 >= 0 and grid[y - 1][x] == '1':
            self.markIsland(grid, y - 1, x)
        if y + 1 < len(grid) and grid[y + 1][x] == '1':
            self.markIsland(grid, y + 1, x)
        if x - 1 >= 0 and grid[y][x - 1] == '1':
            self.markIsland(grid, y, x - 1)
        if x + 1 < len(grid[0]) and grid[y][x + 1] == '1':
            self.markIsland(grid, y, x + 1)
