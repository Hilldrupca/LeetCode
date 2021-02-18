from collections import deque
from typing import List

class TreeNode:
    def __init__(self, val: int =0, left: 'TreeNode' = None,
                 right: 'TreeNode' = None, next: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
    def path(self) -> List[List[int]]:
        '''
        Method to help with testing. Returns the level order of nodes
        using their node.next value
        '''
        node = row = self
        res = [[]]
        while row:
            res[-1].append(node.val)
            node = node.next
            if not node:
                row = row.left
                node = row
                res.append([])
                
        res.pop(-1)
        return res
        
class Solution:
    def connect(self, root: TreeNode) -> TreeNode:
        '''
        Populates each nodes' next point to the node on it's right. Nodes
        along the right most branch will point to None.
        
        **Given a perfect binary tree (all leaves are on the same level, and
        every parent has two children).
        
        Params:
            root - The root TreeNode of a binary tree.
            
        Returns:
            TreeNode - The root TreeNode of a binary tree.
            
        Example:
            Gien the following perfect binary tree:
            
                        1
                       / \
                      /   \
                     2     3
                    / \   / \
                   4   5 6   7
                   
            connect(TreeNode(1)) would result in the following tree:
            
                        1 -> None
                       / \
                      /   \
                    2  ->  3 -> None
                   / \     /\
                  /  |    |  \
                  4->5 -> 6->7 -> None
        '''
        if not root:
            return
        
        row_start = root
        while row_start.left:
            node, prev = row_start, None
            while node:
                if prev:
                    prev.right.next = node.left
                    
                node.left.next = node.right
                
                node, prev = node.next, node
                
            row_start = row_start.left
            
        return root
