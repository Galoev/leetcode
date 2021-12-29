from typing import Optional
from utils import Tree, TreeNode
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return False
    #     if self.isSameTree(root, subRoot):
    #         return True
    #     return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque([root])

        while q:
            node = q.popleft()
            if self.isSameTree(node, subRoot):
                return True
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return False

        
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif (not root and subRoot) or (root and not subRoot):
            return False

        if root.val == subRoot.val:
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)

        return False


if __name__ == "__main__":
    s = Solution()
    # root = Tree.createTree([1,1])
    # subRoot = Tree.createTree([1])
    root = Tree.createTree([3,4,5,1,2])
    subRoot = Tree.createTree([4,1,2,1])
    res = s.isSubtree(root, subRoot)
    print(res)