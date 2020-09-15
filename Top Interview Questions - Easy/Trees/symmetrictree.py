from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        '''
        Determines if a binary tree is symmetrical.
        
        Params:
            root - The root node of a binary tree.
            
        Returns:
            bool - Whether or not a binary tree is symmetrical.
        '''
        if not root:
            return True
        
        left_branch = deque()
        left_branch.append(root.left)
        
        right_branch = deque()
        right_branch.append(root.right)
        
        while left_branch and right_branch:
            left = left_branch.popleft()
            right = right_branch.popleft()
            
            if type(left) != type(right):
                return False
            
            if left and right:
                if left.val != right.val:
                    return False
                left_branch.append(left.left)
                left_branch.append(left.right)
                right_branch.append(right.right)
                right_branch.append(right.left)
            
        return True
