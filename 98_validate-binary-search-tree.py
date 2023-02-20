from typing import Optional
from utils import Tree, TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(v: Optional[TreeNode], min: int, max: int) -> bool:
            if not v: return True
            if v.val <= min: return False
            if v.val >= max: return False
            return check(v.left, min, v.val) and check(v.right, v.val, max)
        
        return check(root, float('-inf'), float('inf'))


if __name__ == "__main__":
    s = Solution()
    nums = [5,4,6,"null","null",3,7]
    root = Tree.createTree(nums)
    print(s.isValidBST(root))
        