from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []

        def visit(node: 'Node'):
            if not node:
                return
            res.append(node.val)
            for c in node.children:
                visit(c)

        visit(root)
        return res

