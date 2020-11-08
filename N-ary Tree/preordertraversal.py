from typing import List

class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
        
class Solution:
    def preorder(self, root: Node) -> List[int]:
        '''
        Given the root node of an n-ary tree, returns the preorder traversal of
        the tree.
        
        Params:
            root - The root node of an n-ary tree.
            
        Returns:
            List[int] - The preorder traversal of the tree.
        '''
        if root is None:
            return []
        
        order = []
        stack = [root]
        while stack:
            node = stack.pop()
            order.append(node.val)
            stack.extend(node.children[::-1])
            
        return order
