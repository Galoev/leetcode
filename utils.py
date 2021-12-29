from typing import List
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.val)
    
class Tree:
    @staticmethod
    def createTree(nums: List[float], node_id=0) -> TreeNode:
        if node_id >= len(nums) or nums[node_id] == "null":
            return None
        root = TreeNode(nums[node_id])
        root.left = Tree.createTree(nums, node_id*2 + 1)
        root.right = Tree.createTree(nums, node_id*2 + 2)
        return root
    
    @staticmethod
    def findNode(root: TreeNode, val: float)  -> TreeNode:
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.val == val:
                return node
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return None
            

