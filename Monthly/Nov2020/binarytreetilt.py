
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    '''
    LeetCode Monthly Challenge problem for November 8th, 2020.
    '''
    def findTilt(self, root: TreeNode) -> int:
        '''
        Given a binary tree, returns the sum of every tree node's tilt.
        
        The tilt of a tree node is the absolute difference between the sum of
        all left subtree node values and all right subtree node values.
        
        Params:
            root - The root node of a binary tree.
            
        Returns:
            int - The sum of all nodes' tils in a binary tree.
            
        Examples:
            Given the following binary tree, a:
                    1
                   / \
                  2   3
                  
            findTilt(a)   ->   1
            
            
            Given the following binary tree, b:
                        4
                       / \
                      2   9
                     / \   \
                    3   5   7
                    
            findTilt(b)   ->   15
            
            
            Given the following binary tree, c:
                            21
                           /  \
                          7    14
                         / \   / \
                        1   1 2   2
                       / \
                      3   3
                      
            findTilt(c)   ->   9
        '''
        def helper(node) -> int:
            if node is None:
                return 0
            
            nonlocal tiltsum
            
            left = helper(node.left)
            right = helper(node.right)
            tiltsum += abs(left-right)
            
            return left + right + node.val
            
        tiltsum = 0
        helper(root)
        
        return tiltsum
