
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    '''
    LeetCode Monthly Challenge problem for November 9th, 2020.
    '''
    def maxAncestorDiff(self, root: TreeNode) -> int:
        '''
        Returns the maxiumum absolute difference between the nodes and their
        ancestors in a binary tree.
        
        Params:
            root - The root node of a binary tree.
            
        Returns:
            int - The maxiumum absolute difference.
            
        Examples:
            Given the following binary tree, a:
            
                        8
                       / \
                      3   10
                     / \    \
                    1   6    14
                       / \   /
                      4   7 13
            
            maxAncestorDiff(a)   ->   7
            
            Given the following binary tree, b:
            
                1
                 \
                  2
                   \
                    0
                   /
                  3
                  
            maxAncestorDiff(b)   ->   3
        '''
        diff = 0
        def helper(node, high, low):
            if node is None:
                return
            
            nonlocal diff
            diff = max(diff, abs(high-node.val), abs(low-node.val))
            high, low = max(high, node.val), min(low, node.val)
            helper(node.left, high, low)
            helper(node.right, high, low)

        helper(root, root.val, root.val)
        return diff
