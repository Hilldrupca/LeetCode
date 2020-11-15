
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    '''
    LeetCode Monthly Challenge problem for November 15th, 2020.
    '''
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        '''
        Returns the sum of node values that fall within a certain range. That
        is, a node's value will be added to the sum if the following condition
        is met:
        
            low <= node.val <= high
            
        Params:
            root - The root node of a binary search tree.
            
            low - The inclusive minimum of a range.
            
            high - The inclusive maximum of a range.
            
        Returns:
            int - The sum of values within a range.
            
        Examples:
            Given the following bst, a:
            
                    10
                   /  \
                  5    15
                 / \     \
                3   7     18
                
            rangeSumBST(a)   ->   32
            
            Given the following bst, b:
            
                    __10__
                   /      \
                  5        15
                 / \      /  \
                3   7   13    18
               /   /
              1   6
              
            rangeSumBST(b)   ->   23
        '''
        sum_range = 0
        def helper(node):
            if not node:
                return
            
            if low <= node.val <= high:
                nonlocal sum_range
                sum_range += node.val
            
            if low < node.val:
                helper(node.left)
            if high > node.val:
                helper(node.right)
            
            
        helper(root)
        return sum_range
