from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        offset_x_right = len(matrix[0]) - 1
        offset_x_left = 0
        offset_y_bottom = len(matrix) - 1
        offset_y_top = 0
        dir = (0, 1)
        cur_index = (0, 0)
        y = len(matrix) - 1
        x = len(matrix[0]) - 1

        def sum_coordinates(dir, index):
            return (dir[0] + index[0], dir[1] + index[1])

        def next(call_count: int):
            if call_count == 4:
                return None
            nonlocal offset_x_right
            nonlocal offset_x_left
            nonlocal offset_y_bottom
            nonlocal offset_y_top 
            nonlocal dir
            new_index = sum_coordinates(dir, cur_index)
            if dir == (0, 1):
                if new_index[1] > offset_x_right:
                    dir = (1, 0)
                    offset_y_top += 1
                    return next(call_count + 1)
            elif dir == (1, 0):
                if new_index[0] > offset_y_bottom:
                    dir = (0, -1)
                    offset_x_right -= 1
                    return next(call_count + 1)
            elif dir == (0, -1):
                if new_index[1] < offset_x_left:
                    dir = (-1, 0)
                    offset_y_bottom -= 1
                    return next(call_count + 1)
            elif dir == (-1, 0):
                if new_index[0] < offset_y_top:
                    dir = (0, 1)
                    offset_x_left += 1
                    return next(call_count + 1)
            
            return new_index

        res = []
        while offset_x_left <= offset_x_right and offset_y_top <= offset_y_bottom:
            res.append(matrix[cur_index[0]][cur_index[1]])
            cur_index = next(0)
            if not cur_index:
                return res
        return res
    

if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(Solution().spiralOrder(matrix))