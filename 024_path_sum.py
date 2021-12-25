from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum -= root.val
        
        if not root.left and not root.right and targetSum==0:
            return True
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

    # def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    #     if not root:
    #         return False
    #     self.targetSum = targetSum
    #     return self.explore(root)

    # def explore(self, node: TreeNode):
    #     if not node.left and not node.right:
    #         if node.val == self.targetSum:
    #             return True
    #         return False
        
    #     res_left = False
    #     if node.left:
    #         node.left.val += node.val
    #         res_left = self.explore(node.left)
        
    #     res_right = False
    #     if node.right:
    #         node.right.val += node.val
    #         res_right = self.explore(node.right)
        
    #     return res_right or res_left


def getTree(nums, root_id=0) -> TreeNode:
    if root_id >= len(nums) or nums[root_id] == "null":
        return None
    root = TreeNode(val=nums[root_id])
    root.left = getTree(nums, root_id=root_id*2 + 1)
    root.right = getTree(nums, root_id=root_id*2 + 2)
    return root

def getStrTree(root, level=0):
    if root:
        ret = "\t"*level+repr(root.val)+"\n"
        ret = ret + getStrTree(root.left, level+1) + getStrTree(root.right, level+1)
        return ret
    return "null"


s = Solution()
# tr = getTree([3,9,20,"null","null",15,7])
tr = getTree([5,4,8,11,"null",13,4,7,2,"null","null","null",1])
print(getStrTree(tr))
print(s.hasPathSum(tr, 22))