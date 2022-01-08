from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        columns = len(matrix[0])

        row_zero = False
        column_zero = False

        for i in range(rows):
            if matrix[i][0] == 0:
                column_zero = True

        for i in range(columns):
            if matrix[0][i] == 0:
                row_zero = True
        


        for i in range(1, rows):
            for j in range(1, columns):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        

        for i in range(1, rows):
            for j in range(1, columns):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        
        if row_zero:
            for i in range(columns):
                matrix[0][i] = 0
        
        if column_zero:
            for i in range(rows):
                matrix[i][0] = 0

    # def setZeroes(self, matrix: List[List[int]]) -> None:
    #     m = len(matrix)
    #     n = len(matrix[0])

    #     zero_idx = []
    #     for i in range(m):
    #         for j in range(n):
    #             if matrix[i][j] == 0:
    #                 zero_idx.append((i, j))
        
    #     for i, j in zero_idx:
    #         self.makeRowAndColZero(matrix, i, j)
    
    # def makeRowAndColZero(self, matrix: List[List[int]], i: int, j: int):
    #     matrix[i] = [0 for _ in range(len(matrix[0]))]
        
    #     for row in matrix:
    #         row[j] = 0



def print_matrix(matrix: List[List[int]]):
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            print(matrix[i][j], " ", end="")
        print()
    

if __name__ == "__main__":
    s = Solution()
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    s.setZeroes(matrix)
    print_matrix(matrix)
