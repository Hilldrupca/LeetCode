'''
Find the sum of all left leaves in a given binary tree.
'''
import warnings
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    '''
    LeetCode Monthly Challenge problem for August 24, 2020
    '''
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        '''
        Finds the sum of all left leaves in a given binary tree.
        
        Params:
            root - The root node in a binary tree of TreeNodes
            
        Returns:
            int - The sum of all left leaves. Returns 0 if root has no children
                  or if it is not an instance of TreeNode.
        '''
        
        if not isinstance(root, TreeNode):
            warnings.warn(f'{type(root)} is not of type {type(TreeNode)}')
            return 0
        
        if not root.left and not root.right:
            return 0
        
        q = deque([(root, None)])
        
        s = 0
        
        # DFS to find left leaves
        while q:
            node, parent = q.popleft()
            
            # Determine if node is a leaf
            if not node.left and not node.right:
                
                # Only add to sum if node is a left leaf
                if node == parent.left:
                    s += node.val
                    
            if node.left:
                q.append((node.left, node))
                
            if node.right:
                q.append((node.right, node))
                
        return s
