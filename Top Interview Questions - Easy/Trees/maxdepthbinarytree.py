from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''
        Finds the maximum depth of a binary tree.
        
        Params:
            root - The root node of a binary tree.
            
        Returns:
            int - The maximum depth of a binary tree. If the the root node
                  has no left or right branches, returns 1. If root node is
                  empty, return 0.
            
        Example:
            Given the following binary tree:
                    3
                   / \
                  9  20
                    /  \
                   15   7
            
            maxDepth()   ->   3
        '''
        if  not root:
            return 0
        
        bfs = deque()
        bfs.append((1, root))
        
        max_depth = 1
        while bfs:
            depth, node = bfs.popleft()
            
            if node.left:
                bfs.append((depth+1, node.left))
                
            if node.right:
                bfs.append((depth+1, node.right))
                
            if depth > max_depth:
                max_depth = depth
                
        return max_depth
