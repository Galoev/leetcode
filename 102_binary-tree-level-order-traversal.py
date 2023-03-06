from typing import Optional
from typing import List
from utils import TreeNode
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        nodes = [root]
        while nodes:
            cur_level_nodes = []
            next_nodes = []
            for node in nodes:
                cur_level_nodes.append(node.val)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            res.append(cur_level_nodes)
            nodes = next_nodes
        
        return res
