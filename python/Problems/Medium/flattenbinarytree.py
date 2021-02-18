
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def _path(self):
        node, res = self, []
        while node:
            res.append(node.val)
            res.append(node.left)
            node = node.right
            
        if res[-1] is None:
            res.pop()
            
        return res
    
class Solution:
    def flatten(self, root: TreeNode) -> None:
        '''
        Flattens a binary tree into a linked list in-place. Meaning every node
        will be moved to the rightmost branch with previously left nodes
        ordered before their repective right nodes.
        
        Params:
            root - The root node of a binary tree.
            
        Returns:
            None - In-place flattening.
            
        Example:
            Below is a binary tree before, and after flattening:
            
                1                   1
               / \                   \
              2   5         ->        2
             / \   \                   \
            3   4   6                   3
                                         \
                                          4
                                           \
                                            5
                                             \
                                              6
        '''
        if not root:
            return
        
        node = root
        while node:
            if node.left:
                left_rightmost = node.left
                while left_rightmost.right:
                    left_rightmost = left_rightmost.right
                    
                node.right, left_rightmost.right = node.left, node.right
                node.left = None
            
            node = node.right
