
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
        
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        '''
        Returns the maximum depth of an n-ary tree.
        
        Params:
            root - The root node of an n-ary tree.
            
        Returns:
            int - The max depth of an n-ary tree.
            
        Examples:
            Given the following n-ary tree, a:
                    1
                   /|\
                  3 2 4
                 / \
                5   6
                
            maxDepth(a)   ->   3
            
            Given the following n-ary tree, b:
                ____1_____
               /   / \    \
              /   /   \    \
             2   3     4    5
                / \    |   / \
               6   7   8  9   10
                   |   |  |
                  11  12  13
                   |
                  14
                  
            maxDepth(b)   ->   5
        '''
        if root is None:
            return 0
        
        def helper(node) -> int:
            if not node.children:
                return 1
            
            depth = 0
            for child in node.children:
                depth = max(depth, helper(child))
                
            return depth + 1
        
        return helper(root)
