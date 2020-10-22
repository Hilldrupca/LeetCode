from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    '''
    LeetCode Monthly Challenge problem for October 22nd, 2020.
    '''
    def minDepth(self, root: TreeNode) -> int:
        '''
        Returns the minimum depth of a binary tree.
        
        # Queue method
        
        Params:
            root - The root node of a binary tree.
            
        Returns:
            int - The minimum depth of a binary tree.
            
        Example:
            Given the following tree, t:
                    3
                   / \
                  9   20
                     /  \
                    15   7
                    
            minDepth(t)   ->   2
        '''
        bfs = deque()
        bfs.append((root, 1))        
        while bfs:
            node, level = bfs.popleft()
            
            if not node:
                continue
            
            if not node.left and not node.right:
                return level
            
            bfs.append((node.left, level + 1))
            bfs.append((node.right, level + 1))
        
        return 0
    
    
    
    def minDepthRecursive(self, root: TreeNode) -> int:
        '''
        Returns the minimum depth of a binary tree. 
        
        # Recursive method.
        
        Params:
            root - The root node of a binary tree.
            
        Returns:
            int - The minimum depth of a binary tree.
            
        Example:
            Given the following tree, t:
                    3
                   / \
                  9   20
                     /  \
                    15   7
                    
            minDepth(t)   ->   2
        '''
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        elif not root.right:
            return self.minDepth(root.left) + 1
        
        elif not root.left:
            return self.minDepth(root.right) + 1
        
        else:
            return min(self.minDepth(root.left),
                       self.minDepth(root.right)) + 1
        
