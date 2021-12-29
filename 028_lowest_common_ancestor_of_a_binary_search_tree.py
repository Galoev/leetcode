from utils import Tree, TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while node:
            if node.val < p.val and node.val < q.val:
                node = node.right
            elif node.val > p.val and node.val > q.val:
                node = node.left
            else:
                return node
        return None
    
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     path_to_p = self.getPathToNode(root, p)
    #     path_to_q = self.getPathToNode(root, q)
    #     len_n = min(len(path_to_p), len(path_to_q))
    #     last_common_node = path_to_p[0]
    #     for i in range(1, len_n):
    #         node_p = path_to_p[i]
    #         node_q = path_to_q[i]
    #         if node_p is not node_q:
    #             break
    #         else:
    #             last_common_node = node_p
    #     return last_common_node

    
    # def getPathToNode(self, root: TreeNode, target: TreeNode) -> list:
    #     node = root
    #     path_to_target = [node]
    #     while node.val != target.val:
    #         if node.val < target.val:
    #             node = node.right
    #         elif node.val > target.val:
    #             node = node.left
    #         path_to_target.append(node)
    #     return path_to_target

if __name__ == "__main__":
    root = Tree.createTree([6,2,8,0,4,7,9,"null","null",3,5])
    s = Solution()
    LCA = s.lowestCommonAncestor(root, Tree.findNode(root, 2), Tree.findNode(root, 4)) 
    print(LCA)