from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.diameter = 0

        self.goDeeper(root)
        return self.diameter

    def goDeeper(self, node: TreeNode):
        if not node:
            return 0
        left = self.goDeeper(node.left)
        right = self.goDeeper(node.right)
        self.diameter = max(self.diameter, left+right)
        return max(left, right) + 1

def getTree(nums, root_id=0) -> TreeNode:
    if root_id >= len(nums) or nums[root_id] == "null":
        return None
    root = TreeNode(val=nums[root_id])
    root.left = getTree(nums, root_id=root_id*2 + 1)
    root.right = getTree(nums, root_id=root_id*2 + 2)
    return root


s = Solution()
# tr = getTree([1,2,3,4,5])
tr = getTree([3,1,"null","null",2])
print(s.diameterOfBinaryTree(tr))