from typing import Optional
from typing import List
from utils import TreeNode
from utils import Tree
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
#         was = deque()
#         was.append((root, 0))
#         res = []
#         while len(was):
#             cur_node, depth = was.popleft()
#             if cur_node.left:
#                 was.append((cur_node.left, depth + 1))
#             if cur_node.right:
#                 was.append((cur_node.right, depth + 1))
    
#             if len(res) <= depth:
#                 res.append([cur_node.val])
#             else:
#                 res[depth].append(cur_node.val)
#         return res[::-1]

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        was = deque()
        was.append(root)
        res = deque()
        while len(was):
            cur_level_nodes = []
            cur_queue_size = len(was)
            for _ in range(cur_queue_size):
                node = was.popleft()
                cur_level_nodes.append(node.val)
                if node.left:
                    was.append(node.left)
                if node.right:
                    was.append(node.right)

            res.appendleft(cur_level_nodes.copy())
        return list(res)


if __name__ == "__main__":
    s = Solution()
    nums = [3,9,20,"null","null",15,7]
    root = Tree.createTree(nums)
    print(s.levelOrderBottom(root))