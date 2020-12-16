
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    '''
    LeetCode Monthly Challenge problem for December 16th, 2020.
    '''
    def isValidBST(self, root: TreeNode) -> bool:
        '''
        Returns whether a binary tree is a binary search tree.
        
        Constraints:
            1 <= # nodes <= 10**4
            -2**31 <= node.val <= 2**31 - 1
            
        Params:
            root - The root node of a binary tree.
            
        Returns:
            bool - Whether the given binary tree is a valid binary search tree.
            
        Examples:
            Given the following binary tree, a:
            
                    2
                   / \
                  1   3
                  
            isValidBST(a)   ->   True
            
            Given the following binary tree, b:
            
                    5
                   / \
                  1   4
                     / \
                    3   6
                    
            isValidBST(b)   ->   False
        '''
        def dfs(root: TreeNode, low: int, high: int) -> bool:
            '''Depth first search helper function.'''
            if not root:
                return True
            
            if low >= root.val or root.val >= high:
                return False
            
            return dfs(root.left, low, root.val) and \
                   dfs(root.right, root.val, high)
               
        return dfs(root, float('-inf'), float('inf'))
