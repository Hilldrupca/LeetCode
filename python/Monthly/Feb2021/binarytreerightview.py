from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    '''
    LeetCode Monthly Challenge problem for February 6th, 2021.
    '''
    def rightSideView(self, root: TreeNode) -> List[int]:
        '''
        Given a binary tree, returns the rightmost nodes of each level ordered
        from top to bottom level.
        
        Params:
            root - The root node of a binary tree.
            
        Returns:
            List[int] - The node values of the rightmost nodes of each level.
                        ordered from top to bottom level.
                        
        Example:
            Given the following binary tree, a:
            
                    1
                   / \
                  2   3
                   \   \
                    5   4
                    
            rightSideView(a)   ->   [1,3,4]
        '''
        def dfs(node, level, view):
            if node is None:
                return
            
            if len(view) == level:
                view.append(node.val)
                
            dfs(node.right, level + 1, view)
            dfs(node.left, level + 1, view)
            
        right_side = []
        dfs(root, 0, right_side)
        
        return right_side
