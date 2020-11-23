
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    '''
    LeetCode Monthly Challenge problem for November 23rd, 2020.
    '''
    def rob(self, root: TreeNode) -> int:
        '''
        The thief has found himself a new place for his thievery again. There
        is only one entrance to this area, called the "root." Besides the root,
        each house has one and only one parent house. After a tour, the smart
        thief realized that "all houses in this place forms a binary tree". It
        will automatically contact the police if two directly-linked houses
        were broken into on the same night.

        Determine the maximum amount of money the thief can rob tonight without
        alerting the police.
        
        Params:
            root - The root node of a binary tree.
            
        Returns:
            int - Maximum amount that can be safely robbed.
            
        Examples:
            Given the following binary tree, a:
            
                        3
                       / \
                      2   3
                       \   \
                        3   1
                        
            rob(a)   ->   7
            
            Given the following binary tree, b:
            
                        3
                       / \
                      4   5
                     / \   \
                    1   3   1
                    
            rob(b)   ->   9
        ''' 
        def helper(root):
            if not root:
                return 0,0
            
            l_prev, l_cur = helper(root.left)
            r_prev, r_cur = helper(root.right)
            
            return l_cur+r_cur, max(l_prev+r_prev+root.val, l_cur+r_cur)
        
        
        return max(helper(root))
