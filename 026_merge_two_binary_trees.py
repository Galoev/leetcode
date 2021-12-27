from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1
        
    # def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    #     node = TreeNode()
    #     root1_val = None
    #     root2_val = None

    #     if root1:
    #         root1_val = root1.val
        
    #     if root2:
    #         root2_val = root2.val
        
    #     if root1_val is not None and root2_val is not None:
    #         node.val = root1_val + root2_val
    #         node.left = self.mergeTrees(root1.left, root2.left)
    #         node.right = self.mergeTrees(root1.right, root2.right)
    #         return node
        
    #     if root1_val is not None:
    #         node.val = root1_val
    #         node.left = root1.left
    #         node.right = root1.right
    #         return node
        
    #     if root2_val is not None:
    #         node.val = root2_val
    #         node.left = root2.left
    #         node.right = root2.right
    #         return node