from typing import Optional
from utils import TreeNode
from utils import Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leaves_val = []
        max_depth = 0
        def visit(v: TreeNode, depth: int):
            nonlocal max_depth
            nonlocal leaves_val
            if not v.left and not v.right:
                if max_depth < depth:
                    max_depth = depth
                    leaves_val = [v.val]
                    return
                leaves_val.append(v.val)
            
            if v.left:
                visit(v.left, depth + 1)
            
            if v.right:
                visit(v.right, depth + 1)
        
        visit(root, 0)
        return sum(leaves_val)


if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4,5,"null",6,7,"null","null",'null','null',8]
    root = Tree.createTree(nums)
    print(s.deepestLeavesSum(root))
        