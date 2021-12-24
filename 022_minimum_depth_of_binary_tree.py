from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque()
        q.append(root)
        depth = 1
        
        while q:
            n = len(q)

            for _ in range(n):
                cur_node = q.popleft()
                if not cur_node.left and not cur_node.right:
                    return depth
                
                if cur_node.left:
                    q.append(cur_node.left)

                if cur_node.right:
                    q.append(cur_node.right)
            
            depth += 1
        
        return depth

    # def minDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     root.level = 1
    #     self.min_level = None
    #     self.explore(root)
    #     return self.min_level

    # def explore(self, v: TreeNode):
    #     if not v.left and not v.right:
    #         if not self.min_level or v.level < self.min_level:
    #             self.min_level = v.level
        
    #     if v.left:
    #         left = v.left
    #         left.level = v.level + 1
    #         self.explore(left)
        
    #     if v.right:
    #         right = v.right
    #         right.level = v.level + 1
    #         self.explore(right)
        



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
tr = getTree([3,9,20,"null","null",15,7])
print(getStrTree(tr))
print(s.minDepth(tr))