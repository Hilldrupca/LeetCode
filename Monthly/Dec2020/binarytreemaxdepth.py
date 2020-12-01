
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    '''
    LeetCode Monthly Challenge problem for December 1st, 2020.
    '''
    def maxDepth(self, root: TreeNode) -> int:
        '''
        Returns the maximum depth of a binary tree.
        
        Params:
            root - The root node of a binary tree.
            
        Returns;
            int - The maximum depth of the given binary tree.
            
        Examples:
            Given the following binary tree, a:
                    
                    3
                   / \
                  9   20
                     /  \
                    15   7
                    
            maxDepth(a)   ->   3
            
            Given the following binary tree, b:
            
                    1
                     \
                      2
                      
            maxDepth(b)   ->   2
        '''
        if not root:
            return 0
        
        return max(self.maxDepth(root.left),
                   self.maxDepth(root.right)) + 1
