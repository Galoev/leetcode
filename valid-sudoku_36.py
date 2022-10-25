from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count_nums_in_rows = [[0 for i in range(9)] for j in range(9)]
        count_nums_in_cols = [[0 for i in range(9)] for j in range(9)]
        count_nums_in_cells = [[0 for i in range(9)] for j in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                num = int(num) - 1
                if count_nums_in_rows[i][num] == 0:
                    count_nums_in_rows[i][num] += 1
                else: return False

                if count_nums_in_cols[j][num] == 0:
                    count_nums_in_cols[j][num] += 1
                else: return False

                cell_id = int(i / 3) * 3 + int(j / 3)
                if count_nums_in_cells[cell_id][num] == 0:
                    count_nums_in_cells[cell_id][num] += 1
                else: return False

        return True


if __name__ == "__main__":
#     board = [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

    board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
    s = Solution()
    print(s.isValidSudoku(board))