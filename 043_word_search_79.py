from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and self.__exist(board, word, i, j):
                    return True
        
        return False
    
    def __exist(self, board: List[List[str]], word: str, i: int, j: int) -> bool:
        if not word:
            return True
        
        m = len(board)
        n = len(board[0])

        if i < 0 or i >= m or j < 0 or j >= n or word[0] != board[i][j]:
            return False
        
        original_val = board[i][j]
        board[i][j] = "_"
        
        res = self.__exist(board, word[1:], i + 1, j) or self.__exist(board, word[1:], i - 1, j) or self.__exist(board, word[1:], i, j + 1) or self.__exist(board, word[1:], i, j - 1)

        board[i][j] = original_val

        return res


# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         if len(word) > (len(board) * len(board[0])):
#             return False

#         start_idxs = self.__get_start_idxs(board, word[0])
        
#         if not start_idxs:
#             return False

#         res = False

#         for i, j in start_idxs:
#             res = res or self.__exist(board, word[1:], i, j, '', [(i, j)])
        
#         return res

#     def __exist(self, board: List[List[str]], word: str, start_i: int, start_j: int, prev_type: str, path: list) -> bool:
#         if not word:
#             return True

#         m = len(board)
#         n = len(board[0])

#         neighbors_idx = self.__get_neighbors_idx(start_i, start_j, m, n, prev_type, path)
#         if not neighbors_idx:
#             return False
        
#         res = False
#         for i, j, _type in neighbors_idx:
#             if board[i][j] == word[0]:
#                 new_path = []
#                 new_path.extend(path)
#                 new_path.append((i, j))
#                 res = res or self.__exist(board, word[1:], i, j, _type, new_path)

#         return res


#     def __get_start_idxs(self, board: List[List[str]], letter: str) -> list:
#         m = len(board)
#         n = len(board[0])

#         res = []
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == letter:
#                     res.append((i,j))
        
#         return res

    
#     def __get_neighbors_idx(self, i, j, m, n, prev_type, path):
#         res = []

#         if prev_type != 'down' and (i - 1) >= 0:
#             up_i = i - 1
#             up_j = j
#             if (up_i, up_j) not in path:
#                 res.append((up_i, up_j, 'up'))

#         if prev_type != 'up' and (i + 1) < m:
#             down_i = i + 1
#             down_j = j
#             if (down_i, down_j) not in path:
#                 res.append((down_i, down_j, 'down'))

#         if prev_type != 'right' and (j - 1) >= 0:
#             left_j = j - 1 
#             left_i = i
#             if (left_i, left_j) not in path:
#                 res.append((left_i, left_j, 'left'))

#         if prev_type != 'left' and (j + 1) < n:
#             right_j = j + 1
#             right_i = i
#             if (right_i, right_j) not in path:
#                 res.append((right_i, right_j, 'right'))

#         return res
        

if __name__ == "__main__":
    s = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED" #True
    # word = "SEE" #True
    # word = "ABCB" #False

    # board = [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]]
    # word = "aaaaaaaaaaaaa" #False

    # board =[["A","A","A","A","A","A"],
    #         ["A","A","A","A","A","A"],
    #         ["A","A","A","A","A","A"],
    #         ["A","A","A","A","A","A"],
    #         ["A","A","A","A","A","B"],
    #         ["A","A","A","A","B","A"]]
    # word = "AAAAAAAAAAAAABB" #False

    print(s.exist(board, word))