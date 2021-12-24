from collections import deque
from typing import Optional, List
from queue import Queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append(root)
        result = []

        while q:
            n = len(q)
            cur_level_sum = 0

            for _ in range(n):
                v = q.popleft()
                cur_level_sum += v.val

                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)

            result.append(cur_level_sum/n)
            
        return result

    # def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    #     q = Queue()
    #     q.put(root)
    #     root.level = 0
    #     level_sums = {0: root.val}
    #     level_count = {0: 1}

    #     while not q.empty():
    #         v = q.get()            
            
    #         if v.left:
    #             left_child = v.left
    #             left_child.level = v.level + 1
                
    #             cur_sum = level_sums.get(left_child.level, 0) + left_child.val
    #             level_sums[left_child.level] = cur_sum

    #             cur_count = level_count.get(left_child.level, 0) + 1
    #             level_count[left_child.level] = cur_count

    #             q.put(left_child)
             
    #         if v.right:
    #             right_child = v.right
    #             right_child.level = v.level + 1
                
    #             cur_sum = level_sums.get(right_child.level, 0) + right_child.val
    #             level_sums[right_child.level] = cur_sum

    #             cur_count = level_count.get(right_child.level, 0) + 1
    #             level_count[right_child.level] = cur_count

    #             q.put(right_child)
        
    #     res = [0 for _ in range(len(level_count))]
    #     for key, val in level_sums.items():
    #         res[key] = float(val)/level_count[key]
    #     return res
        


            

            

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
tr = getTree([3,9,20,15,7])
print(getStrTree(tr))
print(s.averageOfLevels(tr))

