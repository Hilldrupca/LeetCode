from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def _path(self):
        '''Tester method. Returns tree nodes in level order.'''
        res = []
        queue = deque([self])
        
        while queue:
            node = queue.popleft()
            
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
                
        return res
    
class Solution:
    '''
    LeetCode Monthly Challeng problem for February 9th, 2021.
    '''
    def convertBST(self, root: TreeNode) -> TreeNode:
        '''
        Given the root node of a binary search tree, converts the tree to a
        greater tree. Each node will be set equal to it's value plus all node
        values greater than it.
        
        Constraints:
            The number of nodes in the tree is in the range [0, 10**4]
            -10**4 <= node.val <= 10**4
            All the values in the tree are unique
            root is guaranteed to be a valid binary search tree
            
        Params:
            root - The root node of a binary search tree.
            
        Returns:
            TreeNode - The root node of the binary search tree after being
                       converted to a greater tree.
                       
        Example:
            The following binary search tree becomes:
            
                       _4_                     _30_
                      /   \                   /    \
                     1     6                36      21
                    / \   / \       ->     /  \    /  \
                   0   2 5   7            36  35  26   15
                        \     \                 \        \
                         3     8                 33       8
        '''
        def dfs(node: TreeNode, right_sum: int) -> int:
            if node is None:
                return right_sum
            
            node.val += dfs(node.right, right_sum)
            
            return dfs(node.left, node.val)
        
        dfs(root, 0)
        
        return root
