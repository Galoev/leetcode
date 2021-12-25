from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([p, q])

        while queue:
            p_node = queue.popleft()
            q_node = queue.popleft()

            if not p_node and not q_node:
                continue
            
            if not p_node or not q_node:
                return False

            if p_node.val != q_node.val:
                return False
            
            queue.append(p_node.left)
            queue.append(q_node.left)
            queue.append(p_node.right)
            queue.append(q_node.right)
        
        return True
    
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     if not p and not q:
    #         return True
        
    #     if not p or not q:
    #         return False

    #     p_que = deque([p])
    #     q_que = deque([q])

    #     while p_que and q_que:
    #         p_n = len(p_que)
    #         q_n = len(q_que)
            
    #         if p_n != q_n:
    #             return False
            
    #         for _ in range(p_n):
    #             p_node = p_que.popleft()
    #             q_node = q_que.popleft()

    #             if p_node.val != q_node.val:
    #                 return False
                
    #             if p_node.left:
    #                 if q_node.left:
    #                     q_que.append(q_node.left)
    #                     p_que.append(p_node.left)
    #                 else:
    #                     return False
    #             elif q_node.left:
    #                 return False

    #             if p_node.right:
    #                 if q_node.right:
    #                     q_que.append(q_node.right)
    #                     p_que.append(p_node.right)
    #                 else:
    #                     return False
    #             elif q_node.right:
    #                 return False
                    

        
    #     if p_que or q_que:
    #         return False
        
    #     return True

    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     if not p and not q:
    #         return True
        
    #     if not p or not q:
    #         return False

    #     if p.val == q.val:
    #         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    #     return False

def getTree(nums, root_id=0) -> TreeNode:
    if root_id >= len(nums) or nums[root_id] == "null":
        return None
    root = TreeNode(val=nums[root_id])
    root.left = getTree(nums, root_id=root_id*2 + 1)
    root.right = getTree(nums, root_id=root_id*2 + 2)
    return root

def getStrTree(root, level=1):
    if root:
        ret = "\t"*level + str(root.val) + "\n"
        ret = ret + getStrTree(root.left, level+1) + getStrTree(root.right, level+1)
        return ret
    return ""

s = Solution()
# tr = getTree([3,9,20,"null","null",15,7])
p = getTree([1,2,3])
q = getTree([1,2,3])
print(getStrTree(p))
print("-" * 20)
print(f"Answer: {s.isSameTree(p, q)}")
print("-" * 20)