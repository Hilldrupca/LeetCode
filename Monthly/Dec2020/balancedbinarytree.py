
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    '''
    LeetCode Monthly Challange problem for December 22, 2020.
    '''
    def isBalanced(self, root: TreeNode) -> bool:
        '''
        Returns whether the given binary tree is balanced.
        
        Constraints:
            Number of nodes in  the tree is in the range [0, 5000]
            -10**4 <= TreeNode.val <= 10**4
            
        Params:
            root - The root node of a binary tree.
            
        Returns:
            bool - True if the binary tree is balanced, false otherwise.
                   
        Examples:
            Given the following binary tree, a:
            
                    3
                   / \
                  9   20
                     /  \
                    15   7
                    
            isBalanced(a)   ->   4 (True)
            
            Given the following binary tree, b:
            
                    1
                   / \
                  2   2
                 / \
                3   3
               / \
              4   4
              
            isBalanced(b)   ->   False            
        '''
        def helper(root: TreeNode):
            if not root:
                return True
            
            l = helper(root.left)
            r = helper(root.right)
            
            if not l or not r or abs(l-r) > 1:
                return False
            
            return max(l,r) + 1
        
        return helper(root) > 0
